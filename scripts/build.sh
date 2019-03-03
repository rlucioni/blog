#!/usr/bin/env bash
set -ex

node --version
npm --version

npm ci

hugo version

make build
