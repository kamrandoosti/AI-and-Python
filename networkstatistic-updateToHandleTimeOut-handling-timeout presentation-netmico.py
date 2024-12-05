#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 05:14:04 2024

@author: kamran
"""

# modified to handle user input and timeout:

# presenting time out in a more eyecomforting maner


import subprocess
import matplotlib.pyplot as plt
import re

    
from netmiko import ConnectHandler
import time
from datetime import datetime

input_rate_list=[]
output_rate_list=[]
count_list = []
t = -1

# Function to validate user input
def get_monitor_time():
    while True:
        try:
            monitor_time = int(input('Please enter the monitor time to check the 5 minute input/output rate (integer): '))
            return monitor_time
        except ValueError:
            print("Invalid input. Please enter an integer.")

monitor_time = get_monitor_time()

while monitor_time > 0:
    monitor_time -= 1
    t += 1
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
        {"host": "200.200.200.2", "username": "root"}
    ]

    # Merging common configuration with specific details for each device
    devices = [dict(common_config, **details) for details in device_details]

    for device in devices:
        with ConnectHandler(**device) as ssh:
            output = ssh.send_command('show int gig 0/0')
            time.sleep(1)
    show_int_gig = str(output)
    
    # Regular expression to find the response times (updated to handle floating-point numbers)
    input_rate_pattern = r'5 minute input rate ([0-9.]+) bits/sec'
    output_rate_pattern = r'5 minute output rate ([0-9.]+) bits/sec'
    
    # Find all matches of the pattern
    input_rate = re.findall(input_rate_pattern, show_int_gig)
    output_rate = re.findall(output_rate_pattern, show_int_gig)
    # Handle ping timeout or no response time found

    input_rate = float(input_rate[0])
  
    output_rate= float(output_rate[0])
    
 
    input_rate_list.append(input_rate)
    output_rate_list.append(output_rate)
    count_list.append(t)

# Separate lists for successful pings and timeouts
input_rate = [time if time is not None else 0 for time in input_rate_list]
output_rate= [time if time is not None else 0 for time in output_rate_list]
print(input_rate)
print(output_rate)
plt.plot(count_list, input_rate, 'ro-', label='input')
plt.plot(count_list, output_rate, 'bo-', label='output')
plt.legend()
plt.xlabel('Time')
plt.ylabel('RTT (ms)')
plt.title('Ping Statistic')
plt.savefig('/home/kamran/git-test/pingstatistic.png')
plt.show()
