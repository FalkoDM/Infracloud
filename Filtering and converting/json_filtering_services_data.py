### JSON FILTERING -- SERVICES DATA ###

import json

devices_struc = {
 "rack": [
      { "server": { "dev_id": "S1" , "server_name": "svr1" , "domain": "biasc.be", "ip-address": "10.2.3.1" ,
                     "os": "linux"  , "server_type": "vm" ,
                     "services": [   
                       {"service": "ad" , "service_type": "vm", "protocol": "tcp", "port": "389"},
                       {"service": "dns", "service_type": "vm", "protocol": "udp", "port": "53"},
                       {"service": "ntp", "service_type": "vm", "protocol": "udp", "port": "123"} 
                    ]
                  }
      },
      { "server": { "dev_id": "S2" , "server_name": "svr2" , "domain": "biasc.be", "ip-address": "10.2.3.2" ,
                    "os": "linux"  , "server_type": "vm" ,
                    "services": [   
                      {"service": "flask", "service_type": "vm", "protocol": "tcp", "port": "8089"  }, 
                      {"service": "db"   , "service_type": "vm", "protocol": "tcp", "port": "1521"  } 
                    ]     
                 }
      },
      { "server": { "dev_id": "S3" , "server_name": "svr3" ,  "domain": "biasc.be" , "ip-address": "10.2.3.3",
                    "os": "linux"  , "server_type": "vm" ,
                    "services": [   
                      {"service": "dns" , "service_type": "vm", "protocol": "tcp", "port": "8089" }, 
                      {"service": "ntp" , "service_type": "vm", "protocol": "udp", "port": "123" },
                      {"service": "dhcp", "service_type": "docker", "protocol": "udp", "port": "67" }
                    ] 
                  }
      }
   ]
}

print("--V1--")
v1 = json.dumps(devices_struc) # convert dict to string
print(type(v1))

print("--V2--")
v2 = json.loads(v1)   # convert back to dict
print(type(v2))

print("--v3--")
v3 = yaml.dump(v2)  # convert dict generated in v2 to yaml format (type = string)
print(type(v3))
#print(v3)

print("Filter data")
v4 = v2["rack"][0]    # neem enkel de eerste server ==> index 0
print(type(v4))
print(v4["server"].keys())  # print alle keys in de server dict
print(v4["server"]["services"][0].keys())  # print de keys van de server dict, enkel voor de eerste waarde in de services lijst
print(v4["server"]["services"][0].values())

print("Loop trough list")
for v5 in v2["rack"]:
    print(type(v5))
    print(v5["server"]["os"])
    print(v5["server"]["server_name"])
    for v6 in v5["server"]["services"]:
        print(v6)

# print('------1---------')
# print(type(devices_struc))
# print(devices_struc)
# print('------1A--------')
# js_groups = json.dumps(devices_struc)
# print(type(js_groups))
# print(js_groups)
# print('------1B--------')
# print(json.dumps(devices_struc, indent=2))

# print('------2---------')
# for g in devices_struc["rack"]:
#     print('------2A--------')
#     print(type(g))
#     print(g)
#     print(g["server"]["services"])
#     for p in g["server"]["services"]:
#         print(p)
            
# print('------3---------')
# print(devices_struc.keys())
# print('------3A---------')
# print(devices_struc["rack"][0].keys())
# print('------3B---------')
# print(devices_struc["rack"][0]["server"].keys())
# print('------3C---------')
# print(devices_struc["rack"][0]["server"]["services"][0].keys())