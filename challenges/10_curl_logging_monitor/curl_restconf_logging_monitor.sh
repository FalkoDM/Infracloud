#! /bin/bash

IP_HOST=192.168.56.103
USERNAME=cisco
PASSWORD=cisco123!
curl -i -k -X "OPTIONS" "https://$IP_HOST:443/restconf/data/Cisco-IOS-XE-native:native/logging/monitor/severity" \
-H 'Accept: application/yang-data+json' \
-u $USERNAME:$PASSWORD