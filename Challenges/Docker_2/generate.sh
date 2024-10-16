#!/bin/bash

yq '.flag' challenge.yaml > flag.txt


# Script that generates the challenge

python gen.py

docker build . -t docker_2:latest

rm flag.txt

docker save -o img.tar docker_2:latest