import requests
import json

# access token opgehaald op cisco devnet site
current_access_token = "M2FhYmUwZjYtYjY3NS00OGJkLTk5MzctMjcwYjc3ZmY5MWFmNGI2MTNmNWUtODAz_P0A1_ffe50b97-2b4a-4965-8373-9822eafeddfd"
# variables to build an url
uri_scheme = 'https://'
uri_authority_server = 'api.ciscospark.com'
uri_api_path = '/v1/people/me'
url = uri_scheme + uri_authority_server + uri_api_path  # build the url
# headers -h option in the curl statement bash
headers = {
    'Authorization': 'Bearer {}'.format(current_access_token),
    'Content-Type': 'application/json'
}
# do a get request to the url and authorise with the current access token
res = requests.get(url, headers=headers)
# filter the username of the person logged in
user_name = res.json()['displayName']
if res.status_code == 200:
    print("Status is OK")
    print("Username: " + user_name)
else:   
    print("Status is not OK")