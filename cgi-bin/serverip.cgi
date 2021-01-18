#!/usr/bin/python

import subprocess

print("Content-type: text/html\r\n\r\n")

p = subprocess.Popen('/sbin/ifconfig', stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
output, error = p.communicate()

print(output)

