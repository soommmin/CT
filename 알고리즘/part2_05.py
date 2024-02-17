import sys
sys.stdin=open("input.txt", "r")
from collections import deque
import heapq as hq
import itertools as it
import hashlib
import copy 


# 정다면체 

n,m = map(int,input().split())
c = [0]*(n+m+3) 


max = -2147000000 

for i in range(1, n+1):
    for j in range(1, m+1):
        c[i+j] +=1 


for i in range(1, n+m+1):
    if c[i] > max:
        max = c[i] 


for i in range(1, n+m+1):
    if c[i] == max:
        print(i, end = ' ')
