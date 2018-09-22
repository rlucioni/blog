#!/usr/bin/env bash
set -ex

# workaround required to avoid libstdc++ errors while running "extended" hugo with SASS support
wget http://security.ubuntu.com/ubuntu/pool/main/g/gcc-5/libstdc++6_5.4.0-6ubuntu1~16.04.10_amd64.deb
sudo dpkg --force-all -i libstdc++6*.deb

wget -O - https://raw.githubusercontent.com/creationix/nvm/v${NVM_VERSION}/install.sh | bash

set +x
source ~/.nvm/nvm.sh
nvm install
set -x

node --version
npm --version

npm install

wget "https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_Linux-64bit.deb"
sudo dpkg -i hugo*.deb

hugo version
