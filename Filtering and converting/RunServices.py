## json file rack ==> device ==> services

rack_struc = {
    "rack": [
        {"device" : {"dev_id" : "S1",
                     "dev_name": "Server1",
                     "role" : "Server",
                     "ipaddress" : "10.10.10.1",
                     "version" : "version 3.0",
                     "services" : [
                         {"poort": "22" , "protocol" : "tcp" , "Service" : "ssh" , "state" : "filtered" },
                         {"poort": "25" , "protocol" : "tcp" , "Service" : "smtp" , "state" : "open" },
                         {"poort": "80" , "protocol" : "tcp" , "Service" : "http" , "state" : "open" }

                     ]     
                    }
        },
        {"device" : {"dev_id" : "S2",
                     "dev_name": "Server2",
                     "role" : "Server",
                     "ipaddress" : "10.10.10.2",
                     "version" : "version 3.0",
                     "services" : [
                         {"poort": "111" , "protocol" : "tcp" , "Service" : "rpcbind" , "state" : "open" },
                         {"poort": "631" , "protocol" : "tcp" , "Service" : "ipp" , "state" : "open" },
                         {"poort": "3000" , "protocol" : "tcp" , "Service" : "ppp" , "state" : "open" }
                     ]     
                    }
        },
        {"device" : {"dev_id" : "S3",
                     "dev_name": "Server3",
                     "role" : "Server",
                     "ipaddress" : "10.10.10.3",
                     "version" : "version 3.0",
                     "services" : [
                         {"poort": "4000" , "protocol" : "tcp" , "Service" : "remoteanything" , "state" : "open" },
                         {"poort": "8080" , "protocol" : "tcp" , "Service" : "http-proxy" , "state" : "open" },
                         {"poort": "9090" , "protocol" : "tcp" , "Service" : "zeus-admin" , "state" : "open" }
                     ]     
                    }
        }
    ]
}

## print all protocols and services

print("------ALL PORT, PROTOCOLS AND VERSION------")
for g in rack_struc["rack"]:
    print(g["device"]["dev_name"])
    print(g["device"]["ipaddress"])
    print(g["device"]["version"])
    for p in g["device"]["services"]:
        print(p["poort"]+" => "+p["protocol"]+ " => " +p["Service"]+ " => " +p["state"])