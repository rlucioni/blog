# Blog

## Quickstart

Install [Hugo](https://gohugo.io/getting-started/installing/):

    $ brew install hugo

Use [nvm](https://github.com/creationix/nvm) to install Node.js and npm, then install dependencies:

    $ nvm install
    $ npm ci

Start the Hugo server with drafts enabled:

    $ make serve

Create a new post at `content/posts/example.md`:

    $ make post-example

Record terminal session to local file with `asciinema`:

    $ pip install -r requirements.txt
    $ asciinema rec example.cast

## Deployment

Travis CI handles deployment on pushes to master. To build the site for deployment locally:

    $ make build

To run the deployment script locally:

    $ pip install -r requirements.txt
    $ ./scripts/deploy.sh
