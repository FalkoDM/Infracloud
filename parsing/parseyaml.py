# Fill in this file with the code from parsing YAML exercise
import json
import yaml

# open the yaml file with the with statement
with open('myfile.yaml','r') as yaml_file:
    ouryaml = yaml.safe_load(yaml_file) # load the yaml file into a string
print(ouryaml)
print(type(ouryaml)) # output dict
print(f"The access token is {ouryaml['access_token']}.")
print(f"The token expires in {ouryaml['expires_in']} seconds.")

# output the yaml data into json format
print("\n\n")
print(json.dumps(ouryaml, indent=4))

