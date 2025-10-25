#!/usr/bin/env bash
set -ex

if [ -z "$1" ]; then
    echo "error: slug is required"
    echo "usage: $0 <slug>"
    exit 1
fi

SLUG="$1"
DIR="src/posts/$SLUG"

mkdir -p "$DIR"

# generate title from slug (replace hyphens with spaces, capitalize words)
TITLE=$(echo "$SLUG" | sed 's/-/ /g' | awk '{for(i=1;i<=NF;i++){$i=toupper(substr($i,1,1)) tolower(substr($i,2))}}1')
DATE=$(date -u +"%Y-%m-%dT%H:%M:%S-04:00")

cat > "$DIR/index.md" << EOF
---
title: $TITLE
description: TODO
date: $DATE
draft: true
---

TODO
EOF

echo "created new post at $DIR/index.md"

