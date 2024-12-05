#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 05:14:04 2024

@author: kamran
"""

# modified to handle user input and timeout:

import subprocess
import matplotlib.pyplot as plt
import re

ip = '1.1.1.1'
time_list = []
count_list = []
t = -1

# Function to validate user input
def get_monitor_time():
    while True:
        try:
            monitor_time = int(input('Please enter the monitor time to check the ping statistic (integer): '))
            return monitor_time
        except ValueError:
            print("Invalid input. Please enter an integer.")

monitor_time = get_monitor_time()

while monitor_time > 0:
    monitor_time -= 1
    t += 1
    output = subprocess.run(f'ping -c 1 -W 0.2 {ip}', capture_output=True, text=True, shell=True)
    output = output.stdout
    ping_output = str(output)
    
    # Regular expression to find the response times (updated to handle floating-point numbers)
    response_time_pattern = r'time=([0-9.]+) ms'
    
    # Find all matches of the pattern
    response_times = re.findall(response_time_pattern, ping_output)
    
    # Handle ping timeout or no response time found
    if response_times:
        response_time = float(response_times[0])
    else:
        response_time = None
        print(f"Ping attempt {t} failed or timed out.")
    
    # Add the response time to the list (using -1 for timeouts to indicate failure)
    if response_time is not None:
        time_list.append(response_time)
    else:
        time_list.append(-1)
    
    count_list.append(t)

# Print response times and count lists
print("Response times:", time_list)
print("Count:", count_list)

# Plot the results
plt.plot(count_list, time_list, color='red', label='RTT')
plt.legend()
plt.xlabel('Time')
plt.ylabel('RTT (ms)')
plt.title('Ping Statistic')
plt.savefig('/home/kamran/git-test/pingstatistic.png')
plt.show()

