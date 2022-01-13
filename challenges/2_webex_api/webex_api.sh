#! /bin/bash
# access token opgehaald op cisco devnet site / vervalt regelmatig
CURRENT_ACCESS_TOKEN=ZjNiMmQ5Y2QtOGJkNy00Y2I5LTgzN2ItYjljMmI2YzNjMTlkZTFjYTZkMjEtNmU2_P0A1_ffe50b97-2b4a-4965-8373-9822eafeddfd

# url to access the api
URL=https://api.ciscospark.com/v1/people/me

# execute the curl statement below and store the respons in the variable
# -w asks the status code
# -H are the headers to connect with the api trough an access token, and accept the json data
STATUS_CODE=$(curl -ks \
-w "%{http_code}" \
-o /dev/null \
-H "Authorization: Bearer $CURRENT_ACCESS_TOKEN" \
-H "Accept: application/yang-data+json" \
$URL)

# get request to get the personal data from the webex api server like displayname
# -H are the headers for authentication and content type
MY_DATA=$(curl -X GET \
-H "Authorization: Bearer $CURRENT_ACCESS_TOKEN" \
-H "Content-Type: application/json" \
$URL | cut -d '"' -f 14)  # use cut to get the value for displayName

if [ $STATUS_CODE -eq 200 ]
then 
   echo "Status is OK"
   echo "username: $MY_DATA"
else
   echo "Status is NOK"
fi 

# displays all the personal information in a json dict
#echo $MY_DATA

# displays the status code
#echo $status_code

