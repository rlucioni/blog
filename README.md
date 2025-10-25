# Blog

## Quickstart

Use [nvm](https://github.com/creationix/nvm) to install Node.js and npm:

```bash
$ nvm install
$ nvm use
```

Install dependencies:

```bash
$ npm install
```

Start the dev server:

```bash
$ make dev
```

Create a new post at `content/posts/example-slug.md`:

```bash
$ make post slug=example-slug
```

Format code:

```bash
$ make prettier
```

Lint code:

```bash
$ make lint
```

## Deployment

A GitHub Actions workflow handles deployment on pushes to master. To build the site for deployment locally:

```bash
$ make build
```

To run the deployment script locally, install the [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html), then run:

```bash
$ make deploy
```
