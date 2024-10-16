USER='python-www-root'
PASS='KnaprigaKnaprigaTand123'

pacman --noconfirm -Syy
pacman --noconfirm -S firefox python-flask which sudo python python-pip


useradd -m $USER
echo "$USER:$PASS" | chpasswd

#su python-www-root
pacman --noconfirm -S python-markupsafe python-flask-session python-requests
#pip3 install markupsafe
sudo -i -u python-www-root "pip install flask-session"
#pip3 install requests
python3 /srv/init_database.py &
python3 /srv/generate_elevate.py &

