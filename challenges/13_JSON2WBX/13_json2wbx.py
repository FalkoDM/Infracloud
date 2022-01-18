# get access token from https://developer.webex.com
current_access_token = "YWQwOWQ4N2QtMzQxZS00MGY5LWE0YWUtZDQwOTZhZTFhMmE4NDQ2OGU3ODUtMmNh_P0A1_ffe50b97-2b4a-4965-8373-9822eafeddfd"

# import json and webexteamssdk for connection and requests
import json
from webexteamssdk import WebexTeamsAPI
url = WebexTeamsAPI(access_token=current_access_token)

# load the jsonfile into variable jsonfile and close it
with open("webex_groups.json") as file:
    jsonfile = json.load(file)
    file.close()
# jsonfile is loaded as a list but we want a dict
groups = jsonfile["groups"]
# check classes
print("type jsonfile")
print(type(jsonfile))
print("type groups")
print(type(groups))

# for every record in the dict groups, extract the groupname and create the rooms
for record in groups:
    print(record["group"]["group_name"]) # output the records 
    demo_room = url.rooms.create(record["group"]["group_name"]) # api call
    # extract email from  record["group"]["members"] and add it to the respective demo rooms
    for email in record["group"]["members"]:
        url.memberships.create(demo_room.id, personEmail = email["email"])