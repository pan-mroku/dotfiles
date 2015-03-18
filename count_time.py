#!/usr/bin/python

from datetime import datetime
from sys import argv,exit

if len(argv)<2:
    print("No time file.")
    exit(0)

FMT="%H:%M"

def timediff(begin, end):
    diff=datetime.strptime(end, FMT)-datetime.strptime(begin,FMT)
    return diff.seconds

s=0

file=open(argv[1])
for line in file:
    pair=line.strip().split(' ')
    diff=timediff(pair[0], pair[1])
    s+=diff
    print(str(diff/60/60)+":"+str(diff/60%60))


print("---\n"+str(s/60/60)+":"+str(s/60%60))
