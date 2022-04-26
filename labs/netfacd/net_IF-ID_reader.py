#!/usr/bin/env python3

import netifaces

print(netifaces)

print(netifaces.interfaces())

for i in netifaces.interfaces():
    print('\n****** details of interface - ' + i + ' ******')
    try:
        print('MAC: ', end='') # This print statement will always print MAC without an end of line
        print((netifaces.ifaddresses(i)[netifaces.AF_LINK])[0]['addr']) # Prints the MAC address
        print('IP: ', end='')  # This print statement will always print IP without an end of line
        print((netifaces.ifaddresses(i)[netifaces.AF_INET])[0]['addr']) # Prints the IP address
    except:          # This is a new line
        print('Could not collect adapter information') # Print an error message


iface= ""
neti= ""


while iface not in neti:
        iface = input(f{Enter interface name:})
while neti not in iface:


query = input("Display info for which adapter:  n/>")
for i in netifaces.interfaces(query):
    print('\n****** details of interface - ' + i + ' ******')
    
    


    try:
        print('MAC: ', end='') # This print statement will always print MAC without an end of line
        print((netifaces.ifaddresses(i)[netifaces.AF_LINK])[0]['addr']) # Prints the MAC address
        print('IP: ', end='')  # This print statement will always print IP without an end of linelo

        print((netifaces.ifaddresses(i)[netifaces.AF_INET])[0]['addr']) # Prints the IP address
    except:          # This is a new line
        print('Could not collect adapter information') # Print an error messagel

#====================
print(netifaces.interfaces())

def mac(adapter_name):
    print(f"MAC: {netifaces.ifaddresses(adapter_name)[netifaces.AF_LINK][0]['addr']}")

def ip(adapter_name):
    print(f"IP {netifaces.ifaddresses(adapter_name)[netifaces.AF_LINK][0]['addr']}")

choice= input("Choose and adapter \n>")

mac(choice)              # the choice is input as the adapter_name for the function

ip(choice)