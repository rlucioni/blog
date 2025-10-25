#!/usr/bin/env bash
set -ex

npm ci

if [[ "$OS" == "macos" ]]; then
    echo "installing aws cli on macos not supported, exiting"
    exit 0
fi

AWS_VERSION="2.31.22"

# https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-linux.html#cliv2-linux-install
# https://github.com/aws/aws-cli/blob/v2/CHANGELOG.rst
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64-${AWS_VERSION}.zip" -o /tmp/aws.zip
unzip /tmp/aws.zip
sudo ./aws/install -i ~/.aws-cli -b /usr/local/bin
rm /tmp/aws.zip
rm -rf aws

aws --version
