import sys
sys.stdin=open("input.txt", "r")
from collections import deque
import heapq as hq
import itertools as it
import hashlib
import copy 


#백준_2346#

n = int(input())
arr = list(map(int,input().split()))
d = deque()

for i in range(n):
    d.append((arr[i], i+1))

result = []

current, index = d.popleft()
result.append(index)

for i in range(n-1):
    if current > 0:
        for j in range(current-1):
            x = d.popleft()
            d.append(x)

    else:
        for j in range(-current):
            x = d.pop()
            d.appendleft(x)

    current, index = d.popleft()
    result.append(index)

for x in result:
    print(x, end = ' ')
