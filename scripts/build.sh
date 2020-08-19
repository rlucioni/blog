#!/usr/bin/env bash
set -ex

wget "https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_Linux-64bit.tar.gz" -O /tmp/hugo.tar.gz
tar -xvzf /tmp/hugo.tar.gz -C /usr/local/bin

which hugo
hugo version

make build
