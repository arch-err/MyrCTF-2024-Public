#!/bin/sh

mkdir out &>/dev/null
docker save -o out/img.tar docker_1:latest
pushd out &>/dev/null

tar xvf img.tar &>/dev/null
pushd blobs/sha256 &>/dev/null
for file in $(ls -a)
do
    if file $file | grep -q "POSIX tar archive"
    then
        tar xvf $file &>/dev/null
    fi
done


cat rc_additions/passwd.txt

popd &>/dev/null
popd &>/dev/null

rm -rf out
