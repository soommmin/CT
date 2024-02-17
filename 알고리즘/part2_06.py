import sys
sys.stdin=open("input.txt", "r")
from collections import deque
import heapq as hq
import itertools as it
import hashlib
import copy 


# 자릿수의 합 

def digit_sum(x):
    sum = 0 
    while x>0:
        sum += x%10 
        x = x//10 

    return sum 

n = int(input())
a = list(map(int,input().split()))

max = -2147000000
for x in a:
    tot = digit_sum(x)

    if tot > max:
        max = tot 
        res = x 

print(res)