import sys
sys.stdin=open("input.txt", "r")
from collections import deque
import heapq as hq
import itertools as it
import hashlib
import copy 


# k번째 수 


T = int(input())

for t in range(T):
    n,s,e,k = map(int,input().split())
    a = list(map(int,input().split()))
    a = a[s-1:e]
    a.sort()

    print("#%d %d" %(t+1, a[k-1]))