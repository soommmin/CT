import sys
sys.stdin=open("input.txt", "r")
from collections import deque
import heapq as hq
import itertools as it
import hashlib
import copy 


# 랜선자르기(결정알고리즘)

def Count(len):
    cnt = 0 
    for x in Line:
        cnt += (x//len)
    return cnt 

n,k = map(int,input().split())
Line = []


for i in range(n):
    tmp = int(input())
    Line.append(tmp)

Line.sort()

lt = 1
rt = max(Line)


while lt<=rt:
    mid = (lt+rt)//2 

    if Count(mid) < k:
        rt = mid-1 

    else:
        res = mid 
        lt = mid+1 

print(res)
