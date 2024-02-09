import sys
sys.stdin=open("input.txt", "r")
from collections import deque
import heapq as hq
import itertools as it
import hashlib
import copy 


#백준_20040#

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
parent = [0]*n 

for i in range(n):
    parent[i] = i 

cycle = False 
for i in range(m):
    a,b = map(int,input().split())

    if find_parent(parent,a) == find_parent(parent,b):
        cycle = True
        print(i+1)
        break

    else:
        union_parent(parent,a,b)

if not cycle:
    print(0)