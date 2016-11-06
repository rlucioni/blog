"""Task functions for use with Invoke."""
from threading import Thread
import time

from invoke import task
from slugify import slugify


@task(help={
    'watch': 'Regenerate CSS when Sass changes are detected.',
})
def css(context, watch=False):
    """Convert SCSS files to CSS."""
    options = '--style compressed --sourcemap=none'

    if watch:
        cmd = 'sass --watch {scss}:{css} {options}'
    else:
        cmd = 'sass {scss} {css} {options}'

    cmd = cmd.format(scss=context.scss, css=context.css, options=options)

    context.run(cmd)


@task(help={
    'autoreload': 'Regenerate the site when content, theme, or settings are changed.',
})
def build(context, autoreload=False):
    """Build the site."""
    cmd = 'pelican {autoreload} {content} --output {output} --settings {settings}'.format(
        content=context.content,
        output=context.output,
        settings=context.settings,
        autoreload='--autoreload' if autoreload else '',
    )

    context.run(cmd)


@task(help={
    'host': 'Hostname on which to run the server',
    'port': 'Port on which to serve the site',
})
def serve(context, host=None, port=None):
    """Serve the site, refreshing the browser when changes are detected."""
    cmd = 'livereload {directory} --host {host} --port {port}'.format(
        directory=context.output,
        host=host or context.host,
        port=port or context.port,
    )

    context.run(cmd)


@task(help={
    'host': 'Hostname on which to run the server',
})
def stream(context, host=None):
    """
    Serve the site and watch for any content or Sass changes,
    refreshing *the site and the browser* when changes are detected.
    """
    tasks = [
        (css, {'watch': True}),
        (build, {'autoreload': True}),
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


@task(help={
    'title': 'Post title',
    'description': 'Post description',
})
def post(context, title, description):
    """Create a new draft post ready for editing."""
    def timestamp():
        return time.strftime('%Y-%m-%d %H:%M')

    slug = slugify(title.replace("'", ''))
    date = timestamp()

    metadata = [
        'Title: {}'.format(title),
        'Description: {}'.format(description),
        'Slug: {}'.format(slug),
        'Date: {}'.format(date),
        'Modified: {}'.format(date),
        'Author: {}'.format(context.author),
        'Tags: comma, separated, tags',
        'Status: draft',
    ]

    path = '{posts}/{slug}.md'.format(posts=context.posts, slug=slug)

    with open(path, 'w') as f:
        for line in metadata:
            f.write(line + '\n')

        f.write('\n')

    print('File created at {}'.format(path))
