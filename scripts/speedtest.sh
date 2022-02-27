#!/bin/sh

set -xe

apk add wget
apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
python3 -m ensurepip
pip3 install --no-cache --upgrade pip setuptools

python3 scripts/main.py
