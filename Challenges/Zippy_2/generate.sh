#!/bin/bash
depth=30

mkdir archive
yq '.flag' challenge.yaml > archive/flag.txt
ln=archive

7z a 1734.7z -p"1397" -mhe=on archive &>/dev/null
ln=1734.7z

for i in $(seq 1 $depth)
do
	cn=${RANDOM:0:4}
    mkdir $cn

    mv $ln $cn/

    for _ in 1 2 3 4
    do
        touch empty
        7z a $cn/${RANDOM:0:4}.7z empty &>/dev/null
        rm empty
    done
    pass=${ln%.7z}
    # echo $pass

	7z a -p$pass $cn.7z $cn &>/dev/null
	# # zip -r $cn.zip $ln &>/dev/null

	rm -rf $cn &>/dev/null
	ln=$cn.7z
	echo -ne "\r(Zipped $i/$depth)"
done

echo
rm -rf archive
