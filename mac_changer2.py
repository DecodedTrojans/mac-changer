#!/usr/bin/env python

import subprocess
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its mac address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        print("[-]please select the interface")
    elif not options.new_mac:
        print("[-]please input the new MAC address")
    return options
print " "
print "================================================"
print "||  db   db  .d88b.  d8888b. db      d8888b.  || " 
print "||  88   88 .8P  Y8. 88  `8D 88      88  `8D  || " 
print "||  88ooo88 88    88 88oobY' 88      88   88  || "
print "||  88~~~88 88    88 88`8b   88      88   88  || "
print "||  88   88 `8b  d8' 88 `88. 88booo. 88  .8D  || "
print "||  YP   YP  `Y88P'  88   YD Y88888P Y8888D'  || "
print "================================================"
print " "
print "Youtube Channel : https://gplinks.in/6PyAZwRO  "
print "Telegram Channel : https://gplinks.in/eGdvkSv2 "
print ""
def change_mac(interface, new_mac):
    print ("[+] changing mac address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface,  "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface,  "up"])

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print ("[+] colud not read the MAC address.")


options = get_arguments()
current_mac = get_current_mac(options.interface)
print ("Current MAC = " + str(current_mac))
change_mac(options.interface, options.new_mac)
