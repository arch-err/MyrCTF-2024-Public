#!/bin/bash

yq '.flag' challenge.yaml > flag.txt

docker build . -t docker_1:latest

rm flag.txt

docker save -o img.tar docker_1:latest
