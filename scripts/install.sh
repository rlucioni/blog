#!/usr/bin/env bash
set -ex

npm ci

HUGO_VERSION="0.82.0"
HUGO_URL="https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_Linux-64bit.tar.gz"

if [[ "$OS" == "macos" ]]; then
  HUGO_URL="https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_macOS-64bit.tar.gz"
fi

# https://gohugo.io/getting-started/installing/#install-hugo-from-tarball
# https://github.com/gohugoio/hugo/releases
curl -L $HUGO_URL -o /tmp/hugo.tar.gz
sudo tar -xvzf /tmp/hugo.tar.gz -C /usr/local/bin
rm /tmp/hugo.tar.gz

hugo version

if [[ "$OS" == "macos" ]]; then
    echo "installing aws cli on macos not supported, exiting"
    exit 0
fi

AWS_VERSION="2.1.32"

# https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-linux.html#cliv2-linux-install
# https://github.com/aws/aws-cli/blob/v2/CHANGELOG.rst
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64-${AWS_VERSION}.zip" -o /tmp/aws.zip
unzip /tmp/aws.zip
sudo ./aws/install -i ~/.aws-cli -b /usr/local/bin
rm /tmp/aws.zip
rm -rf aws

aws --version
