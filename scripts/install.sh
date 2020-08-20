#!/usr/bin/env bash
set -ex

curl -o /tmp/hugo.tar.gz "https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_Linux-64bit.tar.gz"
tar -xvzf /tmp/hugo.tar.gz -C ~/bin

hugo version

sudo add-apt-repository -y ppa:deadsnakes/ppa
sudo apt-get -q update
sudo apt-get -y install python3.8 python3-pip

python3.8 --version
pip3 --version

pip3 install -r requirements.txt

aws --version
