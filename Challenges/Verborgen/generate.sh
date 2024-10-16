#!/bin/bash

yq '.flag' challenge.yaml > flag.txt

docker build . -t arch3rr/myrctf2024:verborgen-1.0.0

rm ./flag.txt


# Script that generates the challenge
