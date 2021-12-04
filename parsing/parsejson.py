# Fill in this file with the code from parsing JSON exercise
# import json and yaml libraries
import json
import yaml

# use the python with statement to open the myfile.json and set it to the variable json_file
# the json.load method loads the variable into a string and et it to the variable ourjson
with open('myfile.json','r') as json_file:
    ourjson = json.load(json_file) # load json file into a string
print(ourjson)
print(type(ourjson)) # output shows a python dict
print(f"The acces token is: {ourjson['access_token']}") # one way to format
print("The token expires in {} seconds.".format(ourjson['expires_in'])) # another way to format

print("\n\n---") # required 3 dashes for a yaml file
print(yaml.dump(ourjson)) # convert to yaml