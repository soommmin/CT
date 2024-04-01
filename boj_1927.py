import sys
sys.stdin=open("input.txt", "r")
from collections import deque
import heapq as hq
import itertools as it
import hashlib
import copy 


#백준_1927#

n = int(input())
heap = []
result = []

for _ in range(n):
    data = int(input())
    if data == 0:
        if heap:
            result.append(hq.heappop(heap))
        else:
            result.append(0)

    else:
        hq.heappush(heap, data)

for data in result:
    print(data)