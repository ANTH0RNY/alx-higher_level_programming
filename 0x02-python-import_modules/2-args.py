#!/usr/bin/python3
from sys import argv, exit
len = len(argv)
if len - 1 == 1:
    print(f"{len - 1} argument")
else:
    print(f"{len - 1} arguments")
if not (len - 1):
    exit()
for i in range(1,len):
    print(f"{i}: {argv[i]}")