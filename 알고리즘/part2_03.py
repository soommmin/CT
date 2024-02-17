import sys
sys.stdin=open("input.txt", "r")
from collections import deque
import heapq as hq
import itertools as it
import hashlib
import copy 



# K번째 큰 수


n,k = map(int,input().split())
a = list(map(int,input().split()))

res = set()


for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            res.add(a[i]+a[j]+a[m])


res = list(res)
res.sort(reverse=True)
print(res[k-1])