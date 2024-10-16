#!/usr/bin/env bash

steghide extract -sf change_my_mind.jpg -p "" &>/dev/null
# steghide extract -sf change_my_mind.jpg &>/dev/null
exiftool -author fish.jpg | awk '{print $3}'
rm fish.jpg
