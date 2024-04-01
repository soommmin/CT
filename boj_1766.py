import sys
sys.stdin=open("input.txt", "r")
from collections import deque
import heapq as hq
import itertools as it
import hashlib
import copy 


#백준_1766#

n,m = map(int,input().split())
array = [[] for i in range(n+1)]
indegree = [0]* (n+1)

heap = []
result = []

for _ in range(m):
    x,y = map(int,input().split())
    array[x].append(y)
    indegree[y] +=1 

for i in range(1, n+1):
    if indegree[i] == 0:
        hq.heappush(heap, i)

result = []

while heap:
    data = hq.heappop(heap)
    result.append(data)
    for y in array[data]:
        indegree[y] -=1 
        if indegree[y] == 0:
            hq.heappush(heap, y)
    
for i in result:
    print(i, end = ' ')