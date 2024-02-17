import sys
sys.stdin=open("input.txt", "r")
from collections import deque
import heapq as hq
import itertools as it
import hashlib
import copy 


# 대표값

n = int(input())
a = list(map(int,input().split()))

ave = sum(a)/n 
ave = ave+0.5 
ave = int(ave)

min = 2147000000

for idx, x in enumerate(a):
    tmp = abs(x-ave)
    if tmp < min:
        min = tmp 
        score = x 
        res = idx+1 


    elif tmp == min:
        if x > score:
            score = x 
            res = idx+1

print(ave, res)
