USER='php-www-root'
PASS='KnaprigaKnaprigaTand123'

apt update && apt upgrade

apt-get -y install mariadb-server php-cli php-mysql

service mariadb start

useradd -m $USER
echo "$USER:$PASS" | chpasswd

mysqladmin password "thisisbullshit"

mysql -h 127.0.0.1 -u root -pthisisbullshit -e "CREATE USER 'rooti'@'localhost' IDENTIFIED BY 'thisisbullshit'"
mysql -h 127.0.0.1 -u root -pthisisbullshit -e "CREATE DATABASE DBblog CHARACTER SET utf8mb4 COLLATE utf8mb4_swedish_ci"
mysql -h 127.0.0.1 -u root -pthisisbullshit -e "GRANT ALL PRIVILEGES ON DBblog.* TO 'rooti'@'localhost' WITH GRANT OPTION"

mysql -h 127.0.0.1 -u root -pthisisbullshit DBblog < /web/DBblog.sql

rm /web/DBblog.sql
chown -R php-www-root /web
su php-www-root

