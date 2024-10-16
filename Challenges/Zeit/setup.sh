#!/usr/bin/env bash
#!CMD: exit 1
#!CMD: docker-build-run -t zeit:dev -p 8888:8888

USER='tod'
PASS='leben'

pacman --noconfirm -Syy
pacman --noconfirm -S openssh vim perl gnu-netcat
pacman --noconfirm -S python-flask which sudo time timew timeshift




useradd -m $USER
echo "$USER:$PASS"| chpasswd

mkdir /home/$USER/tools
cp $(which timew) /home/$USER/tools/timewarrior
cp $(which timeshift) /home/$USER/tools/timeshift
sudo install -m =xs $(which time) /home/$USER/tools/time



chown -R $USER:$USER /home/$USER
chown -R $USER:$USER /srv
chown root:root /home/$USER/tools/time
chmod u+s /home/$USER/tools/time
