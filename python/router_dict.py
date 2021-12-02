##create dict
ipaddress={"R1":"10.1.1.1","R2":"10.2.2.1","R3":"10.3.3.1"}
print(type(ipaddress))

## add or adapt key value pairs
ipaddress["S1"]="10.1.1.10"
ipaddress["R3"]=["10.3.3.1", "10.3.3.2", "10.3.3.3"]
print(ipaddress)
print(ipaddress["R3"])