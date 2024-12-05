#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 20:45:50 2024

@author: kamran
"""
from netmiko import ConnectHandler
import time
from datetime import datetime
tmd=datetime.now().strftime("%Y-%d-%d %H:%M:%S")
# Common device configuration
common_config = {
    "device_type": "cisco_ios",
    "password": "1234",
    "port": "22",
    "session_log": "log.txt"
}

# Specific device details
device_details = [
    {"host": "100.100.100.2", "username": "test"},
    {"host": "200.200.200.2", "username": "root"},
    {"host": "200.200.250.2", "username": "root"}
]

# Merging common configuration with specific details for each device
devices = [dict(common_config, **details) for details in device_details]

for device in devices:
    with ConnectHandler(**device) as ssh:
        output = ssh.send_command('show int gig 0/0')
        interfaceshow='/home/kamran/git-test' + ssh.find_prompt() + tmd
        ssh.save_config()
        print(output)
        with open(interfaceshow, 'w') as file:
            file.write(output)
        time.sleep(2)


