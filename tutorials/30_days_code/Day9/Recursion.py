#!/bin/python

def factorial(number):
    if number > 1:
        return number * factorial(number-1)
    else:
        return number

n = int(raw_input())

print factorial(n)
