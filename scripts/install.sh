#!/usr/bin/env bash
set -ex

npm ci

export HUGO_VERSION="0.74.3"
export AWS_VERSION="2.0.41"

# https://gohugo.io/getting-started/installing/#install-hugo-from-tarball
# https://github.com/gohugoio/hugo/releases
curl -L "https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_Linux-64bit.tar.gz" -o /tmp/hugo.tar.gz
sudo tar -xvzf /tmp/hugo.tar.gz -C /usr/local/bin
rm /tmp/hugo.tar.gz

hugo version

# https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-linux.html#cliv2-linux-install
# https://github.com/aws/aws-cli/blob/v2/CHANGELOG.rst
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64-${AWS_VERSION}.zip" -o /tmp/aws.zip
unzip /tmp/aws.zip
sudo ./aws/install -i ~/.aws-cli -b /usr/local/bin
rm /tmp/aws.zip
rm -rf aws

aws --version
