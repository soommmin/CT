import sys
sys.stdin=open("input.txt", "r")
from collections import deque
import heapq as hq
import itertools as it
import hashlib
import copy 


# 수들의 합 

n,m = map(int,input().split())
a = list(map(int,input().split()))

lt = 0 
rt = 1 

tot = a[0]
cnt = 0 

while True:
    if tot < m:
        if rt <n:
            tot += a[rt]
            rt +=1 

        else:
            break 

    elif tot == m:
        tot -= a[lt]
        lt +=1 
        cnt +=1 

    else:
        tot -= a[lt]
        lt +=1 

print(cnt)