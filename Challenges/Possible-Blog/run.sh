#!/bin/bash

service mariadb start

while true; do
echo "Running PHP server"
php -S 0.0.0.0:8080 -t /web
sleep 5
done
