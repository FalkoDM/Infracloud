# import json, requests and authenticaiton libraries
import json
import requests
from requests.auth import HTTPBasicAuth
requests.packages.urllib3.disable_warnings() ## disable warnings

#variables needed for connectin and authentication
ipHosts = "192.168.56.103"
username = "cisco"
password = "cisco123!"
url = f"https://{ipHosts}/restconf/data/ietf-interfaces:interfaces"
basicauth = (username, password)

#headers to accept the data in json format ==> curl -H "Accept: application/yang-data+json"
headers = { "Accept": "application/yang-data+json", "Content-type": "application/yang-data+json"}

#build the request and store the response in the variable
response = requests.get(url, auth=basicauth, headers=headers, verify=False)

if response.status_code == 200:
    print(f"yes - interface is up -returning status code: {response.status_code}")
else:
    print(f"No - interface is down - returning status code: {response.status_code}")