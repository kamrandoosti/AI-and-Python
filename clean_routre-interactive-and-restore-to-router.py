#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 00:09:28 2024

@author: kamran
"""


# Open the saved configuration file
# '/home/kamran/R3__2024-12-03_16-38-18.txt'
def clean_router_backup(input_file, output_file, unwanted_patterns):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    cleaned_lines = []
    active_interface = False

    for line in lines:
        # Remove lines containing specific unwanted patterns
        if any(pattern in line for pattern in unwanted_patterns):
            continue

        # Example: Remove empty lines or lines with only whitespace
        if not line.strip():
            continue

        # Check for active interface and add "no shut" if needed
        if "interface" in line:
            if active_interface:
                cleaned_lines.append(" no shut\n")
            active_interface = True
        elif line.startswith("!"):
            if active_interface:
                cleaned_lines.append(" no shut\n")
            active_interface = False

        cleaned_lines.append(line)

    # Add "no shut" to the last active interface if it was active
    if active_interface:
        cleaned_lines.append(" no shut\n")

    with open(output_file, 'w') as file:
        file.writelines(cleaned_lines)

if __name__ == "__main__":
    import sys

    # Get input from user for input and output files and unwanted patterns
    input_file = input("Enter the input file name: ").strip()
    output_file = input("Enter the output file name: ").strip()

    print("Enter unwanted patterns (enter ezch pattern and \n hit enter for adding next \n pattern \ at the end type 'done' to finish):")
    unwanted_patterns = []
    while True:
        pattern = input().strip()
        if pattern.lower() == 'done':
            break
        unwanted_patterns.append(pattern)

    clean_router_backup(input_file, output_file, unwanted_patterns)
    print(f"Cleaned configuration saved to {output_file}")
    
from netmiko import ConnectHandler

# Define the router's 
router_ip = input('enter ip addreess: ').str
username = input('enter usernamme: ')


# dictionary with the device information
device = {
    'device_type': 'cisco_ios',
    'host': router_ip,
    'username': username,
    'password': '1234',
}

connect_R2 = ConnectHandler(**device)

# Open the saved configuration file
with open(output_file, 'r') as file:
    config_commands = file.readlines()

# Enter configuration mode and send the commands
connect_R2.enable()
output = connect_R2.send_config_set(config_commands)
print(output)

# Save the configuration and exit
connect_R2.send_command('write memory')
connect_R2.disconnect()