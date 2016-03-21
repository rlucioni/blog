"""Task functions for use with Invoke."""
from threading import Thread
import time

from invoke import call, ctask as task
from slugify import slugify


def timestamp():
    return time.strftime('%Y-%m-%d %H:%M')


@task(help={
    'title': 'Post title',
    'description': 'Post description',
    'author': 'Name of the post author',
})
def post(context, title, description, author=None):
    """Create a new draft post and open it for editing."""
    slug = slugify(title.replace("'", ''))
    date = timestamp()

    metadata = [
        'Title: {}'.format(title),
        'Description: {}'.format(description),
        'Slug: {}'.format(slug),
        'Date: {}'.format(date),
        'Modified: {}'.format(date),
        'Author: {}'.format(author or context.author),
        'Tags: GOT TAGS BRO?',
        'Status: draft',
    ]

    path = '{posts}/{slug}.{extension}'.format(
        posts=context.posts,
        slug=slug,
        extension=context.extension,
    )

    with open(path, 'w') as f:
        for line in metadata:
            f.write(line + '\n')

        f.write('\n')

    context.run('open {}'.format(path))


@task(help={
    'scss': 'Path to input SCSS file',
    'css': 'Path at which to output generated CSS file',
    'watch': 'Regenerate CSS when SCSS files are changed',
})
def css(context, scss=None, css=None, watch=False):
    """Generate CSS from SCSS."""
    options = '--style compressed --sourcemap=none'

    if watch:
        cmd = 'scss --watch {scss}:{css} {options}'
    else:
        cmd = 'scss {scss} {css} {options}'

    cmd = cmd.format(
        scss=scss or context.scss,
        css=css or context.css,
        options=options,
    )

    context.run(cmd)


@task(help={
    'content': 'Path to content files',
    'output': 'Path at which to output generated files',
    'settings': 'Path to settings module',
    'autoreload': 'Regenerate the site when content, theme, or settings are changed.',
})
def site(context, content=None, output=None, settings=None, autoreload=False):
    """Generate the site."""
    cmd = 'pelican {autoreload} {content} --output {output} --settings {settings}'.format(
        content=content or context.content,
        output=output or context.output,
        settings=settings or context.settings.dev,
        autoreload='--autoreload' if autoreload else '',
    )

    context.run(cmd)


@task(help={
    'directory': 'Directory to watch for changes',
    'host': 'Hostname on which to run the server',
    'port': 'Port on which to serve the site',
})
def serve(context, directory=None, host=None, port=None):
    """Serve the site, refreshing the browser when changes are detected."""
    cmd = 'livereload {directory} --host {host} --port {port}'.format(
        directory=directory or context.output,
        host=host or context.host,
        port=port or context.port,
    )

    context.run(cmd)


@task(help={
    'host': 'Hostname on which to run the server',
})
def stream(context, host=None):
    """Serve the site and watch for changes, refreshing the site and the browser when changes are detected."""
    tasks = [
        (css, {'watch': True}),
        (site, {'autoreload': True}),
        (serve, {'host': host}),
    ]

    threads = [
        Thread(target=target, args=(context,), kwargs=kwargs, daemon=True)
        for target, kwargs in tasks
    ]

    [t.start() for t in threads]
    [t.join() for t in threads]


@task
def clean(context):
    """Remove generated files and directories."""
    generated = ' '.join(context.generated)
    cmd = 'rm -rf {generated}'.format(generated=generated)

    context.run(cmd)


@task(
    pre=[css, call(site, settings='configuration/production.py')]
)
def publish(context):
    """Publish the site to GitHub Pages."""
    cmd = 'ghp-import -m "Publish site" -p {output}'.format(
        output=context.output
    )

    context.run(cmd)
