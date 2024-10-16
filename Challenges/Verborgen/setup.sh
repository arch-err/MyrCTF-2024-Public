#!/usr/bin/env bash
#!CMD: exit 1
#!CMD: docker-build-run -t verborgen:dev -p 8888:8888

USER='verborgen'
PASS='verborgen'

pacman --noconfirm -Syy
pacman --noconfirm -S openssh vim perl gnu-netcat
pacman --noconfirm -S python-flask which sudo



useradd -m $USER
echo "$USER:$PASS"| chpasswd

mkdir /home/$USER/{Documents,Videos,Desktop}
mkdir /home/$USER/Videos/.․
sudo install -m =xs $(which find) /home/$USER/Videos/.․/
rm /usr/bin/find # >:)


chown -R $USER:$USER /home/$USER
chown -R $USER:$USER /srv
chown root:root /home/$USER/Videos/.․/find
chmod u+s /home/$USER/Videos/.․/find
# chown -R $USER:$USER /home/.hidden
