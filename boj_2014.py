import sys
sys.stdin=open("input.txt", "r")
from collections import deque
import heapq as hq
import itertools as it
import hashlib
import copy 


#백준_2014#

k,n = map(int,input().split())
data = list(map(int,input().split()))

heap = []
visited = set()
max_value = max(data)

for x in data:
    hq.heappush(heap, x)

for i in range(n-1):
    element = hq.heappop(heap)
    for x in data:
        now = element * x 

        if len(heap) >= n and max_value < now:
            continue
        if now not in visited:
            hq.heappush(heap, now)
            max_value = max(max_value, now)
            visited.add(now)

print(hq.heappop(heap))
