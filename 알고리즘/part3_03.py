import sys
sys.stdin=open("input.txt", "r")
from collections import deque
import heapq as hq
import itertools as it
import hashlib
import copy 



# 카드 역배치

a = list(range(21))

for i in range(10):
    s,e = map(int,input().split())

    for j in range((e-s+1)//2):
        a[s+j],a[e-j] = a[e-j], a[s+j]

a.pop(0)

for x in a:
    print(x, end = ' ')