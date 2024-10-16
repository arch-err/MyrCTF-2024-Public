#!/bin/bash

git clone "https://github.com/py-er/basemulticoder.git" 2>/dev/null

python basemulticoder/basemulticoder.py -si "MYRCTF{DABASE}" -o ingrediens.encoded -m encode64 -t 45

rm -rf basemulticoder
