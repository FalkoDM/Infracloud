# import json module, open the file and load it in variable jsonObject
import json
with open("info.js") as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()

# use filters to obtain specific data
containerId = jsonObject[0]['Id']
creationDate = jsonObject[0]['Created']
status = jsonObject[0]['State']['Status']
name = jsonObject[0]['Name']
hostPort = jsonObject[0]['HostConfig']['PortBindings']['5059/tcp'][0]['HostPort']
hostName = jsonObject[0]['Config']['Hostname']
ipAddress = jsonObject[0]['NetworkSettings']['IPAddress']
gateway = jsonObject[0]['NetworkSettings']['Gateway']
macAddress = jsonObject[0]['NetworkSettings']['MacAddress']

# print out the results of filtering
print(f"containerId: {containerId[0:5]}")
print(f"Creation date: {creationDate}")
print(f"Status: {status}")
print(f"Name: {name}")
print(f"Host Port: {hostPort}")
print(f"Hostname: {hostName}")
print(f"IP Address: {ipAddress}")
print(f"Gateway: {gateway}")
print(f"Mac Address: {macAddress}")