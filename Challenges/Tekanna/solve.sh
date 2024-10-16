#!/bin/bash

IP="localhost:8888"

ALPHABET="abcdefghijklmnopqrstuvwxyz"

codes=""
message=""

save_codes=false

while true
do
	curl -s $IP -o .tmp
	sleep 0.2
	code=$(cat .tmp | cut -d" " -f1)

	if [[ $code == "508" ]]
	then
		if test -z "$codes"
		then
			save_codes=true
		else
			break
		fi
	elif $save_codes
	then
		codes="$codes $code"
	fi
done

stripped_codes=$(echo $codes | sed "s/\( \|^\)4/ /g")


for code in $stripped_codes
do
	code=$(echo $code | sed "s/^0\+//")
	code=$(($code - 1))
	message=$message$(echo ${ALPHABET:$code:1})
done
echo
echo Message: $message
echo "Flag: MyrCTF{$message}"

rm .tmp
