#!/usr/bin/python3
import sys
import subprocess as sp


x = ""
y = []

def factors2(public):
        i = (int(public))
        xd = int(x)
        if xd % i == 0:
                y.append([xd, xd // i, i])

with open(sys.argv[1]) as file:
    for line in file:
        x = line.rstrip()
        str2 = "factor " + str(x)
        output = sp.getoutput(str2)
        y = output.split() 

print("{}={}*{}".format(y[0][:-1],y[-1], int(y[0][:-1])//int(y[-1])))
