import sys
sys.stdin=open("input.txt", "r")
from collections import deque
import heapq as hq
import itertools as it
import hashlib
import copy 


#백준_1939#

n,m = map(int,input().split())
adj = [[] for _ in range (n+1)]

def bfs(c):
    queue = deque([start_node])
    visitied = [False] * (n+1)
    visitied[start_node] = True
    while queue:
        x = queue.popleft()
        for y, weight in adj[x]:
            if not visitied[y] and weight >= c:
                visitied[y] = True
                queue.append(y)
    return visitied[end_node]


start = 1000000000
end = 1 

for _ in range(m):
    x,y,weight = map(int,input().split())
    adj[x].append((y,weight))
    adj[y].append((x,weight))
    start = min(start, weight)
    end = max(end, weight)

start_node , end_node = map(int,input().split())

result = start
while(start <= end):
    mid = (start+end) //2 
    if bfs(mid):
        result = mid 
        start = mid+1 

    else:
        end = mid-1 

print(result)