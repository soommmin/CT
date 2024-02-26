import sys
sys.stdin=open("input.txt", "r")
from collections import deque
import heapq as hq
import itertools as it
import hashlib
import copy 

# 공주 구하기(큐)

n,k = map(int,input().split())
q=list(range(1, n+1))
dq = deque(q)

while dq:
    for _ in range(k-1):
        cur = dq.popleft()
        dq.append(cur)

    dq.popleft()
    if len(dq) == 1:
        print(dq[0])
        dq.popleft()