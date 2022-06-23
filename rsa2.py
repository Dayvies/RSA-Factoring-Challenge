#!/usr/bin/python3
import sys
from functools import reduce
def factors(n):
    step = 2 if n % 2 == 0 else 1
    return [i for i in range(2, int(n**0.5) + 1, step) if n % i == 0]


with open(sys.argv[1]) as file:
    for line in file:
        i = (int(line.rstrip()))
        l = factors(i)
        print(l)
