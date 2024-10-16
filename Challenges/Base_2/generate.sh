#!/bin/bash

git clone "https://github.com/py-er/basemulticoder.git" 2>/dev/null

python basemulticoder.py -si "MYRCTF{16_32_64}" -o resultat.encoded -m encoderand -t 27

rm -rf basemulticoder