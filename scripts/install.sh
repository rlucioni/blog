#!/usr/bin/env bash
set -ex

curl -L "https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_Linux-64bit.tar.gz" -o /tmp/hugo.tar.gz
tar -xvzf /tmp/hugo.tar.gz -C ~/bin

hugo version

curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o /tmp/aws.zip
unzip /tmp/aws.zip
./tmp/aws/install --help
./tmp/aws/install -i /tmp -b ~/bin

aws --version
