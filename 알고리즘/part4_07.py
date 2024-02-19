import sys
sys.stdin=open("input.txt", "r")
from collections import deque
import heapq as hq
import itertools as it
import hashlib
import copy 


# 창고 정리 

L = int(input())
a = list(map(int,input().split()))
m = int(input())
a.sort()

for _ in range(m):
    a[0] +=1 
    a[L-1] -=1
    a.sort()

print(a[L-1]-a[0])