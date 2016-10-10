#!/bin/python

import sys

def break_string(input_string):
    even = ''
    odd = ''
    length = len(input_string)
    if length == 1:
        return [input_string, '']
    else:
        for i in range(0, length-1, 2):
            even += input_string[i]
            odd += input_string[i+1]
    if length % 2 ==  1:
        even += input_string[-1:]
    return [even, odd]

n = int(raw_input().strip())

for i in range(0, n):
    string = raw_input()
    even_odd = break_string(string)
    print even_odd[0], even_odd[1]
    

