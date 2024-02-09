import sys
sys.stdin=open("input.txt", "r")
from collections import deque
import heapq as hq
import itertools as it
import hashlib
import copy 


#백준_11286#

heap = []

n = int(input())
for i in range(n):
    x = int(input())
    if x == 0:
        if len(heap) == 0:
            print(0)

        else:
            absolute,original = hq.heappop(heap)
            print(original)
    else:
        hq.heappush(heap, (abs(x),x))