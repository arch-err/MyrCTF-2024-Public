#!/usr/bin/env bash

USER='u40036659'
PASS='859274791047572897314392752'

pacman --noconfirm -Syy
pacman --noconfirm -S python-flask




useradd -m $USER
echo "$USER:$PASS" | chpasswd

mkdir /home/$USER/

chown -R $USER:$USER /home/$USER
chown -R $USER:$USER /srv
