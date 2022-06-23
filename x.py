#!/usr/bin/python3
import subprocess as sp
output = sp.getoutput('factor 34567893')
print (output.split())