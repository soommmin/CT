import sys
sys.stdin=open("input.txt", "r")
from collections import deque
import heapq as hq
import itertools as it
import hashlib
import copy 


#백준_1021#

n,m = map(int,input().split())
d = deque([i for i in range(1, n+1)])
targets = list(map(int,input().split()))
cnt = 0

for target in targets:
    index = d.index(target)
    if index <= len(d)//2:
        for i in range(index):
            x = d.popleft()
            d.append(x)
            cnt +=1 

    else:
        for i in range(len(d)- index):
            x = d.pop()
            d.appendleft(x)
            cnt +=1 

    d.popleft()
print(cnt)
