#!/usr/bin/env bash
set -ex

aws s3 cp public s3://renzo.lucioni.xyz \
  --recursive \
  --exclude "*" \
  --include "*.js" \
  --include "*.css" \
  --cache-control "max-age=31536000"

aws s3 cp public s3://renzo.lucioni.xyz \
  --recursive \
  --exclude "*" \
  --include "*.html" \
  --cache-control "no-cache"

aws s3 cp public s3://renzo.lucioni.xyz \
  --recursive \
  --exclude "*.js" \
  --exclude "*.css" \
  --exclude "*.html" \
  --cache-control "max-age=86400"

aws s3 sync public s3://renzo.lucioni.xyz --delete

aws cloudfront create-invalidation --distribution-id $CLOUDFRONT_DISTRIBUTION_ID --paths "/*"
