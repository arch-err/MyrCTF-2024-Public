#!/bin/bash

## Solution

# like a zip layer challange, theres a layer for each letter in the flag, in each layer, theres 1000 files with seamingly random content, but the most common letter in each layer is part of the flag.

# The challange here is to extract all layers in order and get the most common letter for each part of the flag


# Script to solve the challenge
mkdir -p out
sudo docker save -o out/out.tar docker2
sudo chown $USER out/out.tar

tar xf out/out.tar -C out/

python solve.py


rm -rf out