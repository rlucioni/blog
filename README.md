# Blog

## Quickstart

Install Hugo:

    $ brew install hugo

Create a new post:

    $ hugo new posts/example.md

Start the Hugo server with drafts enabled:

    $ make serve

Build the site for deployment:

    $ make build

## Deployment

Deployment to S3 is handled by [Travis](.travis.yml) on builds of the master branch. For more details, see [this post](https://renzo.lucioni.xyz/s3-deployment-with-travis).
