import os
import sys
import csv
from csv import reader
from pathlib import Path
from typing import List, TextIO

# gets current file path
cwd = os.getcwd()

# gets system platform
os_platform = sys.platform

# makes file contents a dictionary
with open('devices.csv') as csvfile:
    reader = csv.DictReader(csvfile, skipinitialspace=True)
    d = {name: [] for name in reader.fieldnames}
    for row in reader:
        for name in reader.fieldnames:
            d[name].append(row[name])


row_count = len(d)

# new "output" dir is created and txt script is created
# Path("Output").mkdir(parents=True, exist_ok=True)


print("===========")

print("Starting script...\n===========")

print("There is " + str(row_count) + " addresses listed in linux-dhcp-reservation.csv\n")

with open('devices.csv') as csvfile:
    # Return a reader object which will
    # iterate over lines in the given csvfile.
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:


# with open('devices.csv', 'r') as f:
#  file = csv.reader(f)
#  my_list = list(file)
# print(my_list)

      #  maclist = open("linux-dhcp-reservation.txt", "r")
      #  read_file = csv.reader(maclist)
        with open('linux-dhcp-reservation.txt', 'w') as f:
            print("# linux-dhcp-reservation\n\n", file=f)
            for row in readCSV:
                sys.stdout = f  # Change the standard output to the file we created.
                print('host', row[1],'{', file=f)
                print('hardware ethernet', row[0], file=f)
                print('fixed-address', row[2], file=f)
                print('}',file=f)
                print("\n", file=f)
     #   maclist.close()

# print("===========\nScript finished!\n")





