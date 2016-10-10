#!/bin/python

import sys

n = int(raw_input().strip())
# arr = map(int,raw_input().strip().split(' '))
names = []
numbers = []
phonebook = {}
for i in range(0, n):
    line = raw_input().strip().split(' ')
    names.append(line[0])
    numbers.append(line[1])
phonebook = dict(zip(names, numbers))

while True:
    try:
        next = raw_input().strip()
    except:
        break
    try:
        print '{}={}'.format(next, phonebook[next])
    except:
        print 'Not found'
    
