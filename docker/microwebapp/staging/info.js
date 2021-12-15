[
    {
        "Id": "0c5a06d5cddcbf7111ccf39da1b794c32e00636fc2eb804903cfb74868379bdd",
        "Created": "2021-12-15T11:30:20.870097457Z",
        "Path": "/bin/sh",
        "Args": [
            "-c",
            "python /home/microweb_app/micro.py"
        ],
        "State": {
            "Status": "running",
            "Running": true,
            "Paused": false,
            "Restarting": false,
            "OOMKilled": false,
            "Dead": false,
            "Pid": 83854,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2021-12-15T11:30:21.262199659Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:c69db13e10def062f0de2abb64af25e2cb48b78854ec6b9397427beabc9461c5",
        "ResolvConfPath": "/var/lib/docker/containers/0c5a06d5cddcbf7111ccf39da1b794c32e00636fc2eb804903cfb74868379bdd/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/0c5a06d5cddcbf7111ccf39da1b794c32e00636fc2eb804903cfb74868379bdd/hostname",
        "HostsPath": "/var/lib/docker/containers/0c5a06d5cddcbf7111ccf39da1b794c32e00636fc2eb804903cfb74868379bdd/hosts",
        "LogPath": "/var/lib/docker/containers/0c5a06d5cddcbf7111ccf39da1b794c32e00636fc2eb804903cfb74868379bdd/0c5a06d5cddcbf7111ccf39da1b794c32e00636fc2eb804903cfb74868379bdd-json.log",
        "Name": "/micro",
        "RestartCount": 0,
        "Driver": "overlay2",
        "Platform": "linux",
        "MountLabel": "",
        "ProcessLabel": "",
        "AppArmorProfile": "docker-default",
        "ExecIDs": null,
        "HostConfig": {
            "Binds": null,
            "ContainerIDFile": "",
            "LogConfig": {
                "Type": "json-file",
                "Config": {}
            },
            "NetworkMode": "default",
            "PortBindings": {
                "5059/tcp": [
                    {
                        "HostIp": "",
                        "HostPort": "5059"
                    }
                ]
            },
            "RestartPolicy": {
                "Name": "no",
                "MaximumRetryCount": 0
            },
            "AutoRemove": false,
            "VolumeDriver": "",
            "VolumesFrom": null,
            "CapAdd": null,
            "CapDrop": null,
            "CgroupnsMode": "host",
            "Dns": [],
            "DnsOptions": [],
            "DnsSearch": [],
            "ExtraHosts": null,
            "GroupAdd": null,
            "IpcMode": "private",
            "Cgroup": "",
            "Links": null,
            "OomScoreAdj": 0,
            "PidMode": "",
            "Privileged": false,
            "PublishAllPorts": false,
            "ReadonlyRootfs": false,
            "SecurityOpt": null,
            "UTSMode": "",
            "UsernsMode": "",
            "ShmSize": 67108864,
            "Runtime": "runc",
            "ConsoleSize": [
                0,
                0
            ],
            "Isolation": "",
            "CpuShares": 0,
            "Memory": 0,
            "NanoCpus": 0,
            "CgroupParent": "",
            "BlkioWeight": 0,
            "BlkioWeightDevice": [],
            "BlkioDeviceReadBps": null,
            "BlkioDeviceWriteBps": null,
            "BlkioDeviceReadIOps": null,
            "BlkioDeviceWriteIOps": null,
            "CpuPeriod": 0,
            "CpuQuota": 0,
            "CpuRealtimePeriod": 0,
            "CpuRealtimeRuntime": 0,
            "CpusetCpus": "",
            "CpusetMems": "",
            "Devices": [],
            "DeviceCgroupRules": null,
            "DeviceRequests": null,
            "KernelMemory": 0,
            "KernelMemoryTCP": 0,
            "MemoryReservation": 0,
            "MemorySwap": 0,
            "MemorySwappiness": null,
            "OomKillDisable": false,
            "PidsLimit": null,
            "Ulimits": null,
            "CpuCount": 0,
            "CpuPercent": 0,
            "IOMaximumIOps": 0,
            "IOMaximumBandwidth": 0,
            "MaskedPaths": [
                "/proc/asound",
                "/proc/acpi",
                "/proc/kcore",
                "/proc/keys",
                "/proc/latency_stats",
                "/proc/timer_list",
                "/proc/timer_stats",
                "/proc/sched_debug",
                "/proc/scsi",
                "/sys/firmware"
            ],
            "ReadonlyPaths": [
                "/proc/bus",
                "/proc/fs",
                "/proc/irq",
                "/proc/sys",
                "/proc/sysrq-trigger"
            ]
        },
        "GraphDriver": {
            "Data": {
                "LowerDir": "/var/lib/docker/overlay2/ea447ec2d3c1f1b6415d59ad78c571503ba2fa04910ea567250d88dbcce2ef15-init/diff:/var/lib/docker/overlay2/43b8f7e25cfac749148275c2fe30a95fb10614580ef0125f8ea23c3e79fefc20/diff:/var/lib/docker/overlay2/41158bf23c7f7ed74ce1988d6617b6331be41d19fb5d97b1652706795415ff44/diff:/var/lib/docker/overlay2/e66f3f6bf11e4f13f2245d92b9d7dddead37a1fe6ab5f3a5d51bdb650adac839/diff:/var/lib/docker/overlay2/b5cd2f31f80eca562810183d059350c0f2ec757f91ce7aa60de11664a381d2db/diff:/var/lib/docker/overlay2/95f36322240bd147b1c2727510fbd89dcdefd72f57688902b1801cf8abd39069/diff:/var/lib/docker/overlay2/cec74dee18ae2121d77aa62eff4d1da1d79af68244b1b633ad6d5c74d29478d6/diff:/var/lib/docker/overlay2/cee91d0de627b1d45fb52b7a6f080c5e20fc4c4a524e3a760ac1863c14fac8b2/diff:/var/lib/docker/overlay2/da693714a2c4f83e0394fd91e3b50ed5083c9a324fdccbff9615da1a0c3998ce/diff:/var/lib/docker/overlay2/d890c35f22c8d32f8a2f4d32c24337d45d54bb756044d31b4d2719bad69ae5de/diff:/var/lib/docker/overlay2/199017ff8bf6d0e030f895e92178f7d900541b213c7348afefc85044e0c9b918/diff:/var/lib/docker/overlay2/08fefdaf1188a2c8b5bbedae9aabc683ae1bb6dc4c4213354478ac33de0ee727/diff:/var/lib/docker/overlay2/7df51938d438f6faccf4c3e6bc90c80c6219d693fcd06b762a0320eab47fcea3/diff:/var/lib/docker/overlay2/a66fde9916f25f68b3b6c83b5e2f4514ac808a9b02c4431f7f00c7192f955c82/diff",
                "MergedDir": "/var/lib/docker/overlay2/ea447ec2d3c1f1b6415d59ad78c571503ba2fa04910ea567250d88dbcce2ef15/merged",
                "UpperDir": "/var/lib/docker/overlay2/ea447ec2d3c1f1b6415d59ad78c571503ba2fa04910ea567250d88dbcce2ef15/diff",
                "WorkDir": "/var/lib/docker/overlay2/ea447ec2d3c1f1b6415d59ad78c571503ba2fa04910ea567250d88dbcce2ef15/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "0c5a06d5cddc",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "ExposedPorts": {
                "5059/tcp": {}
            },
            "Tty": true,
            "OpenStdin": false,
            "StdinOnce": false,
            "Env": [
                "PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
                "LANG=C.UTF-8",
                "GPG_KEY=A035C8C19219BA821ECEA86B64E628F8D684696D",
                "PYTHON_VERSION=3.10.1",
                "PYTHON_PIP_VERSION=21.2.4",
                "PYTHON_SETUPTOOLS_VERSION=57.5.0",
                "PYTHON_GET_PIP_URL=https://github.com/pypa/get-pip/raw/3cb8888cc2869620f57d5d2da64da38f516078c7/public/get-pip.py",
                "PYTHON_GET_PIP_SHA256=c518250e91a70d7b20cceb15272209a4ded2a0c263ae5776f129e0d9b5674309"
            ],
            "Cmd": [
                "/bin/sh",
                "-c",
                "python /home/microweb_app/micro.py"
            ],
            "Image": "microweb",
            "Volumes": null,
            "WorkingDir": "",
            "Entrypoint": null,
            "OnBuild": null,
            "Labels": {}
        },
        "NetworkSettings": {
            "Bridge": "",
            "SandboxID": "e4e15dd63004e15228883bcc8ffa3655287d94fa3f17e262c5260745576a9f5d",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {
                "5059/tcp": [
                    {
                        "HostIp": "0.0.0.0",
                        "HostPort": "5059"
                    },
                    {
                        "HostIp": "::",
                        "HostPort": "5059"
                    }
                ]
            },
            "SandboxKey": "/var/run/docker/netns/e4e15dd63004",
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "7bf07ab53c1e48fafb73c89fb36553cabbec576b5190a61c2e90d8717b85bee2",
            "Gateway": "172.17.0.1",
            "GlobalIPv6Address": "",
            "GlobalIPv6PrefixLen": 0,
            "IPAddress": "172.17.0.2",
            "IPPrefixLen": 16,
            "IPv6Gateway": "",
            "MacAddress": "02:42:ac:11:00:02",
            "Networks": {
                "bridge": {
                    "IPAMConfig": null,
                    "Links": null,
                    "Aliases": null,
                    "NetworkID": "35ce33c2a41f3b97114f5aedeee778e094d0a15c505fd778c90f543e4dab273b",
                    "EndpointID": "7bf07ab53c1e48fafb73c89fb36553cabbec576b5190a61c2e90d8717b85bee2",
                    "Gateway": "172.17.0.1",
                    "IPAddress": "172.17.0.2",
                    "IPPrefixLen": 16,
                    "IPv6Gateway": "",
                    "GlobalIPv6Address": "",
                    "GlobalIPv6PrefixLen": 0,
                    "MacAddress": "02:42:ac:11:00:02",
                    "DriverOpts": null
                }
            }
        }
    }
]
