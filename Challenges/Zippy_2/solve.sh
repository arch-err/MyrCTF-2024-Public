#!/bin/bash
#!CMD: ./solve.sh *.7z
#!CMD: rm *.7z flag.txt; ./generate.sh && ./solve.sh *.7z

[[ $1 == "" ]] && echo "Usage: $0 <archive.archive>" && exit 1
echo "If it seems like the script has stopped: press enter"

# Arguments: archive.7z
function crack() {
    seq 0 9999 > numbers.lst


    7z2john "$1" > hash

    mv ~/.john/john.pot ~/.john/john.pot.disabled
    john hash --wordlist=numbers.lst > john.out

    pass=$(grep "($1)" john.out | awk '{print $1}')

    if ! echo $pass | grep -qP "[0-9]{4}"
    then
        echo "Error: Could not crack archive."
        exit 1
    fi

    7z x "$1" -p$pass -so | grep MYRCTF > flag.txt

    # Cleanup
    mv ~/.john/john.pot.disabled ~/.john/john.pot
    rm numbers.lst john.out hash
}



archive=$1

while true
do
	[[ $archive == "" ]] && exit 0


    if ! 7z l $archive -ba &>/dev/null
    then
	    # [[ $archive == "1734.7z" ]] || crack $archive
	    crack $archive
        rm $archive
        archive=""
        continue
    fi

    for subarc in $(7z l $archive -ba | grep -Po '\d+/\d+\.7z')
    do
        pass=$(echo $subarc | cut -d"/" -f2 | perl -pe "s/.7z$//")

        if 7z e "$archive" -p$pass &>/dev/null
        then
            rm -rf $archive $(echo $archive | perl -pe "s/.7z$//")
            break
        fi
    done


    for newarcs in $(ls *.7z)
    do
        if 7z l -pxxx $newarcs -ba | grep -q "empty"
        then
            rm $newarcs
        fi
    done


	archive=$(ls *.7z)

	i=$(($i+1))
	echo -ne "\r(Unzipped: $i)"
done
echo
