import sys
sys.stdin=open("input.txt", "r")
from collections import deque
import heapq as hq
import itertools as it
import hashlib
import copy 


# 마구간 정하기(결정알고리즘)
def Count(len):
    cnt = 1 
    ep = Line[0]
    for i in range(1, n):
        if Line[i]- ep >= len:
            cnt +=1 
            ep = Line[i]

    return cnt

n,c = map(int,input().split())
Line = []
for _ in range(n):
    tmp=int(input())
    Line.append(tmp)
Line.sort()

lt = 1
rt = n-1 


while lt<=rt:
    mid = (lt+rt)//2 

    if Count(mid) < c:
        rt = mid-1 

    else:
        res = mid 
        lt = mid+1 

print(res)