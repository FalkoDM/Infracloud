# import the libraries needed for this challenge
import json
import requests
from dotenv import load_dotenv # dotenv reads the variables stored in a .env file 
import os # environment variables are implemented trough the os package
requests.packages.urllib3.disable_warnings()

api_url = "https://192.168.56.103/restconf/data/ietf-interfaces:interfaces"
load_dotenv() # load the credentials stored in the .env file
basicauth = (os.environ.get("username"), os.environ.get("password")) # use these environemnt variables with the os.environ.get function
# notice how the variables aren't hard coded but stored in a different file / location

headers = {"Accept": "application/yang-data+json", "content-type": "application/yang-data+json"} # accept yang data + json
# store the response from the get request below in the variable
response = requests.get(api_url, auth = basicauth, headers=headers, verify=False)
response_json = response.json() # transform it to json format
print(json.dumps(response_json, indent=4)) # format it to readable json