#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 05:14:04 2024

@author: kamran
"""

import subprocess as subprocess
import matplotlib.pyplot as plt
import sys
import time
import re

ip = '1.1.1.1'
time_list = []
count_list = []
t=-1
monitor_time=int(input('please enter the monitor time to check the ping statistic: '))
while monitor_time > 0:
    monitor_time=monitor_time-1
    t=t+1
    output = subprocess.run(f'ping -c 1 -W 2 {ip}', capture_output=True, text=True, shell=True)
    output = output.stdout
    ping_output = str(output)
    
    # Regular expression to find the response times (updated to handle floating-point numbers)
    response_time_pattern = r'time=([0-9.]+) ms'
    
    # Find all matches of the pattern
    response_times = re.findall(response_time_pattern, ping_output)
    response_times=float(response_times[0])
    # Convert the response times to floats
    time_list.append(response_times)
    count_list.append(t)
    
# print("Response times:", time_list)
# print("Response times:", count_list)

plt.plot(count_list, time_list, color='red', label='RTT')
plt.legend()
plt.xlabel('tiem')
plt.ylabel('RTT')
plt.title('this is the ping statistic')
plt.savefig('/home/kamran/git-test/pingstatistic.png')
