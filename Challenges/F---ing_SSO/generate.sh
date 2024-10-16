#!/usr/bin/env bash

yq '.flag' challenge.yaml > flag.txt

docker build . -t arch3rr/myrctf2024:fuckingsso-1.0.1

rm ./flag.txt
