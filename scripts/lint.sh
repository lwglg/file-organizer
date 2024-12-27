#!/usr/bin/env bash

set -e
set -x

mypy fileorganizer
black fileorganizer --check
isort fileorganizer --check-only
