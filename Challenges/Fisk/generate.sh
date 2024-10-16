#!/usr/bin/env bash

inFileCMM="change_my_mind.jpg"
inFileF="fish.jpg"


cp in/$inFileCMM ./
cp in/$inFileF ./

exiftool -author="$(yq '.flag' challenge.yaml)" "$inFileF"
steghide embed -ef "$inFileF" -cf "$inFileCMM" -p ""

rm $inFileF "$inFileF"_original
