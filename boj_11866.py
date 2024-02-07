import sys
sys.stdin=open("input.txt", "r")
from collections import deque
import heapq as hq
import itertools as it
import hashlib
import copy 


#백준_11866#

n,k = map(int,input().split())

d = deque([i for i in range(1, n+1)])
result = []

for i in range(n):
    for i in range(k-1):
        x = d.popleft()
        d.append(x)
    x = d.popleft()
    result.append(x)


print('<', end = '')
for i in range(len(result)):
    if i < len(result)-1:
        print(result[i], end = ', ')
    else:
        print(result[i], end = '')
print('>')