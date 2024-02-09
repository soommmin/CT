import sys
sys.stdin=open("input.txt", "r")
from collections import deque
import heapq as hq
import itertools as it
import hashlib
import copy 


#백준_11724#

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a<b:
        parent[b] = a 

    else:
        parent[a] = b 


n,m = map(int,input().split())
parent = [0]*(n+1)

for i in range(1, n+1):
    parent[i] = i 

for i in range(m):
    a,b = map(int,input().split())
    union_parent(parent, a,b)

counter = set()
for i in range(1, n+1):
    counter.add(find_parent(parent,i))

print(len(counter))