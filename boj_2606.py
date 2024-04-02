import sys
sys.stdin=open("input.txt", "r")
from collections import deque
import heapq as hq
import itertools as it
import hashlib
import copy 


#백준_2606#

n = int(input())
m = int(input())

adj = [[] for _ in range(n+1)]
visitied = [False] * (n+1)
count = 0 

for _ in range(m):
    x,y = map(int,input().split())
    adj[x].append(y)
    adj[y].append(x)


def dfs(now_pos):
    global count 
    count +=1 

    visitied[now_pos] = True
    for next_pos in adj[now_pos]:
        if not visitied[next_pos]:
            dfs(next_pos)

dfs(1)
print(count - 1)