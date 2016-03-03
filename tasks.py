"""Task functions for use with Invoke."""
from threading import Thread

from invoke import ctask as task


@task(help={
    'content': 'Path to content files',
    'output': 'Path at which to output generated files',
    'settings': 'Path to settings module',
})
def regenerate(context, content=None, output=None, settings=None):
    """Regenerate the site every time a change is detected."""
    cmd = 'pelican --autoreload {content} --output {output} --settings {settings}'.format(
        content=content or context.content,
        output=output or context.output,
        settings=settings or context.settings,
    )

    context.run(cmd)


@task(help={
    'scss': 'Path to input SCSS file',
    'css': 'Path at which to output generated CSS file',
})
def scsswatch(context, scss=None, css=None):
    """Regenerate CSS every time changes to SCSS files are detected."""
    cmd = 'scss --watch {scss}:{css} --style compressed --sourcemap=none'.format(
        scss=scss or context.scss,
        css=css or context.css,
    )

    context.run(cmd)


@task(help={
    'directory': 'Directory to watch for changes',
    'port': 'Port on which to serve the site',
})
def livereload(context, directory=None, port=None):
    """Start a `livereload` server."""
    cmd = 'livereload {directory} --port {port}'.format(
        directory=directory or context.output,
        port=port or context.port,
    )

    context.run(cmd)


@task
def serve(context):
    """Serve the site, reloading it as it changes."""
    threads = [
        Thread(target=t, args=(context,), daemon=True)
        for t in (regenerate, scsswatch, livereload)
    ]

    [t.start() for t in threads]
    [t.join() for t in threads]
