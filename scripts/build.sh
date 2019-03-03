#!/usr/bin/env bash
set -ex

wget -O - https://raw.githubusercontent.com/creationix/nvm/v${NVM_VERSION}/install.sh | bash

set +x
source $HOME/.nvm/nvm.sh
nvm install
set -x

npm install -g npm@${NPM_VERSION}

node --version
npm --version

npm ci
pip install -r requirements.txt

hugo version

make build
