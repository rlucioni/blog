# Blog

## Quickstart

Use [nvm](https://github.com/creationix/nvm) to install Node.js and npm:

    $ nvm install
    $ nvm use

Install dependencies, including [Hugo](https://gohugo.io):

    $ make install OS=macos

Start the Hugo server with drafts enabled:

    $ make serve

Create a new post at `content/posts/example.md`:

    $ make post-example

To record a local terminal session, install Python dependencies then run `asciinema`:

    $ pip install -r requirements.txt
    $ asciinema rec example.cast

## Deployment

A GitHub Actions workflow handles deployment on pushes to master. To build the site for deployment locally:

    $ make build

To run the deployment script locally, install the [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html), then run:

    $ make deploy

To submit a newly deployed sitemap to Google:

    $ make ping
