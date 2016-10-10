#!/bin/python

import sys

arr = []
for arr_i in xrange(6):
   arr_temp = map(int,raw_input().strip().split(' '))
   arr.append(arr_temp)

sums = []

for i in range(4):
   for j in range(4):
        hourglass = arr[i][j:3+j] + arr[i+1][j+1:j+2] + arr[i+2][j:3+j]
        sums.append(sum(hourglass))
print max(sums)
