#!/usr/bin/env python3

import subprocess
import optparse

interface = input("interface > ")
new_mac = input("new MAC >")

print("[+] Changing MAC address for " + interface + " to " + new_mac)

#attacker able to hijack and insert additional commands 
subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)

#program will not be used to run additional commands

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])