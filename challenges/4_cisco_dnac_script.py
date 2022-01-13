import requests
import datetime
import json
requests.packages.urllib3.disable_warnings()
print ("Current date and time: ")
print(datetime.datetime.now())
# Variables to build the token request url
DNAC_scheme = 'https://'
DNAC_authority='sandboxdnac.cisco.com'
DNAC_port=':443'
DNAC_path_token='/dna/system/api/v1/auth/token'
DNAC_path='/dna/intent/api/v1/network-device'
#### variables to authenticate
DNAC_user = input("Username? ") 
DNAC_psw = input("Password? ")  
#REQUEST TOKEN BASED ON USERNAME AND PASSWORD
token_req_url = DNAC_scheme+DNAC_authority+DNAC_path_token
auth = (DNAC_user, DNAC_psw)
req = requests.post(token_req_url, auth=auth, verify=False)
## after the request is done, print out the desired values
print("API Return Code: " + str(req.status_code))  
print('Request URI: ' + token_req_url)
print("Username: " + DNAC_user)
resp = req.text
token = req.json()['Token']
print("Received Token:")
print(token)
print("Length Token:")
print(len(token))
