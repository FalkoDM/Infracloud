# import json, requests and authenticaiton libraries
import json
import yaml
import requests
from requests.auth import HTTPBasicAuth
requests.packages.urllib3.disable_warnings() ## disable warnings

#variables needed for connectin and authentication
ipHosts = "192.168.56.103"
username = "cisco"
password = "cisco123!"
url = f"https://{ipHosts}:443/restconf/data/Cisco-IOS-XE-native:native/logging/monitor/severity"
basicauth = (username, password)

#headers to accept the data in json format ==> curl -H "Accept: application/yang-data+json"
headers = { "Accept": "application/yang-data+json", "Content-type": "application/yang-data+json"}

#build the request and store the response in the variable
response = requests.options(url, auth=basicauth, headers=headers, verify=False) # use options instead of get to get the needed info

# use print(dir(response)) to dig into the filesystem and concactenate the information like version, status, and reason
print(response.raw.version, response.raw.status, response.raw.reason)

# loop trough the items in the headers and print the key value pairs
for k, v in response.headers.items():# most of the info is stored in the headers
    print(f"{k}: {v}")

