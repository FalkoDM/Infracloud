### create json structure, rack ==> device ==> interfaces

rack_struc = {
    "rack": [
        {"device" : {"dev_id" : "D1",
                     "dev_name": "R1",
                     "role" : "router",
                     "interfaces" : [
                         {"interface": "GigabitEthernet1" , "ipaddress" : "172.18.1.1" , "subnet_mask" : "255.255.255.0" },
                         {"interface": "GigabitEthernet2" , "ipaddress" : "172.18.3.1" , "subnet_mask" : "255.255.255.0" },
                         {"interface": "GigabitEthernet3" , "ipaddress" : "172.18.4.1" , "subnet_mask" : "255.255.255.0" }
                     ]     
                    }
        },
        {"device" : {"dev_id" : "D2",
                     "dev_name": "C1",
                     "role" : "core",
                     "interfaces" : [
                         {"interface": "VLAN1" , "ipaddress" : "172.18.1.2" , "subnet_mask" : "255.255.255.0" },
                         {"interface": "VLAN2" , "ipaddress" : "172.18.2.1" , "subnet_mask" : "255.255.255.0" },
                         {"interface": "VLAN20" , "ipaddress" : "172.18.20.1" , "subnet_mask" : "255.255.255.0" }
                     ]     
                    }
        },
        {"device" : {"dev_id" : "D3",
                     "dev_name": "AC",
                     "role" : "access",
                     "interfaces" : [
                         {"interface": "VLAN2" , "ipaddress" : "172.18.2.2" , "subnet_mask" : "255.255.255.0" }
                     ]     
                    }
        }
    ]
}

## transfer data to yaml

import yaml
yaml_data = yaml.dump(rack_struc)
print(yaml_data)

## transfer data to xml

from dicttoxml import dicttoxml
xml_data = dicttoxml(rack_struc)
print (xml_data)


## print all the functions

import xlrd
print(dir(xlrd))

### all device + interfaces + ip address

print("------ALL DEVICES INTERFACES IP ADRESSES------")
for g in rack_struc["rack"]:
    print(g["device"]["dev_name"])
    for p in g["device"]["interfaces"]:
        print(p["interface"]+" => "+p["ipaddress"])