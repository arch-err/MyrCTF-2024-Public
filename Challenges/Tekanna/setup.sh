#!/usr/bin/env bash
#!CMD: docker-build-run -t tekanna:dev -p 8888:8888

USER='teapot'
PASS='teapot'

pacman --noconfirm -Syy
pacman --noconfirm -S openssh vim perl gnu-netcat
pacman --noconfirm -S python-flask which sudo



useradd -m $USER
echo "$USER:$PASS"| chpasswd

mkdir /home/$USER/{Documents,Videos,Desktop}


chown -R $USER:$USER /home/$USER
chown -R $USER:$USER /srv
