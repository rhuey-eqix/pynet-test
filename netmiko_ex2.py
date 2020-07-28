'''Simple script to use netmiko'''

import os
from getpass import getpass
from pprint import pprint
from netmiko import ConnectHandler

#password = getpass()

def filename()
    '''return device name'''
    
def save_file(filename, show_run):
    """Save the show run to a file"""
    with open(filename, "w") as f:
        f.write(show_run)

sros1 = {
    "device_type": "nokia_sros",
    "host": "sros.lasthop.io",
    "username": "admin",
    "password": "admin",
    "port": "2211",
}

vmx1 = { 
    "device_type": "juniper_junos",
    "host": "vmx1.lasthop.io",
    "username": "pyclass",
    "password": "88newclass",
}

#pprint(device)

for device in (sros1, vmx1): 
    net_connect = ConnectHandler(**device)
    print()
    print(f"Host: {net_connect.host}:{net_connect.port}")
    print("_" * 50)
    print()

    print(net_connect.find_prompt())
    #output = net_connect.send_command("show system license")

    print()
    print(net_connect.send_command("show version"))

    if "nokia_sros" is device["device_type"]:
        output = net_connect.send_command("admin display-config")
    elif "juniper_junos" is device["device_type"]:
        output = net_connect.send_command("show configuration")

    #print(output)
    #print("_" * 50)

    filename(**device)

    #filename = net_connect.base_prompt + ".txt"
    print("Save show run output: {}\n".format(filename))
    save_file(filename, output)
    
    net_connect.disconnect()
