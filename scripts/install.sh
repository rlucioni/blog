#!/usr/bin/env bash
set -ex

npm ci

# https://gohugo.io/getting-started/installing/#install-hugo-from-tarball
# https://github.com/gohugoio/hugo/releases
curl -L "https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_Linux-64bit.tar.gz" -o /tmp/hugo.tar.gz
tar -xvzf /tmp/hugo.tar.gz -C ~/bin

hugo version

# https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-linux.html#cliv2-linux-install
# https://github.com/aws/aws-cli/blob/v2/CHANGELOG.rst
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64-${AWS_VERSION}.zip" -o /tmp/aws.zip
unzip /tmp/aws.zip
./aws/install -i ~/aws-cli -b ~/bin

aws --version
