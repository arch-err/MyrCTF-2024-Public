#!/bin/bash

git clone "https://github.com/py-er/basemulticoder.git" 2>/dev/null

python basemulticoder.py -fi resultat.encoded -m decode

rm -rf basemulticoder