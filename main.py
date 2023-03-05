import os
import sys
# import csv
from csv import reader
from pathlib import Path

# gets current file path
cwd = os.getcwd()

# gets system platform
os_platform = sys.platform

open_file = open('devices.csv')
read_file = reader(open_file)

# makes file contents a dictionary
devices = dict(read_file)
# devices = csv.DictReader(read_file)
# removes column headers
del devices["MAC"]

num_of_addr = len(devices)

# new "output" dir is created and txt script is created
Path("Output").mkdir(parents=True, exist_ok=True)

if os_platform == "win32":
    new_script = open("Output\\linux-dhcp-reservation.txt", "w")
else:
    new_script = open("Output/linux-dhcp-reservation.txt", "w")

print("===========")
print("There is " + str(num_of_addr) + " addresses listed in linux-dhcp-reservation.csv\n")

print("Starting script...\n===========")
print("  MAC Address                Name            IP")
print("  ----------                 ------          ------")

new_script.write("# linux-dhcp-reservation\n\n")

# List of address object names
address_objects = [1]

for addr, mac in devices.items():
    # Adds address object names to address_objects list
    address_object = str(mac)  # str(addr) + str(mac)
    address_objects.append(address_object)

    # Writes fortigate script to file
    new_script.write(
        "host {mac} {{ \nhardware ethernet {addr}\nfixed-address {mac}\n}}\n\n".format(addr=addr, mac=mac))
    print("Added {addr}    {mac}".format(addr=addr, mac=mac))

new_script.write("# end\n")
new_script.close()

print("===========\nScript finished!\n")
