#!/usr/bin/python3
import sys
import subprocess as sp


x = ""
with open(sys.argv[1]) as file:
    for line in file:
        x = line.rstrip()
        str2 = "factor " + str(x)
        output = sp.getoutput(str2)
        y = output.split()
        print("{}={}*{}".format(y[0][:-1], int(y[0][:-1])//int(y[1]), y[1]))
