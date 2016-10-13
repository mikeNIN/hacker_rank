#!/bin/python


"""
The Utopian Tree goes through 2 cycles of growth every year. Each spring,
it doubles in height. Each summer, its height increases by 1 meter.

How tall will her tree be after N growth cycles?

Solution is basic geometric series of odd numbers

Sn = SUM(n=1, inf)a1 * pow(q, n-1) for q = 2

"""

import sys

def powerChunk(q, n):

    if n == 1:
        return q*n
    else:
        return pow(q, n)
            

def calculateSeries(n):
    if n == 0:
        return 1
    if n  ==  1:
        return 2
    else:
        # let's see how many odd numbers
        len_series = n/2
        if n%2 != 0:
            len_series += 1
        sum = 0
        for i in xrange(1, len_series+1):
            sum += powerChunk(2, i)
            
        # if n is even than we need to add one to final score
        if n%2 == 0:
            return sum + 1
        return sum


t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    print calculateSeries(n)
