#!/usr/bin/env bash
set -ex

# https://gohugo.io/getting-started/installing/#install-hugo-from-tarball
curl -L "https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_Linux-64bit.tar.gz" -o /tmp/hugo.tar.gz
tar -xvzf /tmp/hugo.tar.gz -C ~/bin

hugo version

# https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-linux.html#cliv2-linux-install
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o /tmp/aws.zip
unzip /tmp/aws.zip -d /tmp
./tmp/aws/install --help
./tmp/aws/install -i /tmp -b ~/bin

aws --version
