#!/bin/bash

IN=RC_ClusterSecrets_QA2.7z

7z x $IN -y
cd ${IN%.7z}
# git log
CID=$(git rev-list --all | xargs git grep key | cut -d":" -f1)

git checkout $CID
cp key.txt ../
git switch -
export SOPS_AGE_KEY=$(grep AGE-SECRET-KEY ../key.txt)
rm ../key.txt

echo ""
echo ""
echo ""
sops --decrypt secret-xztrace-alloyToken.enc.yaml | yq ".data.token" | base64 -d
rm -rf ${IN%.7z}
