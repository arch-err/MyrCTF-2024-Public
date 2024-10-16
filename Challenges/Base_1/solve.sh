#!/bin/bash

git clone "https://github.com/py-er/basemulticoder.git" 2>/dev/null

python basemulticoder/basemulticoder.py -fi ingrediens.encoded -m decode

rm -rf basemulticoder
