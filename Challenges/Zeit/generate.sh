#!/bin/bash

FLAG=$(yq '.flag' challenge.yaml)

sed -i "s/MYRCTF{.*}/$FLAG/" generateCert.sh

DATE="$(date +%m/02/%Y)"
shc -e $DATE -m "You are too late, this code expired on $DATE. You are no longer allowed to run this code." -r -f generateCert.sh -o root/generateCert

docker build . -t tod:1.0.0
