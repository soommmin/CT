import sys
sys.stdin=open("input.txt", "r")
from collections import deque
import heapq as hq
import itertools as it
import hashlib
import copy 


#백준_13335#

n,w,l = map(int,input().split())
trucks = list(map(int,input().split()))
trucks.reverse()


q = deque()
total = 0 
t = 0 


while True:
    if len(trucks) == 0 and total == 0:
        break

    if len(q) == w:
        x = q.popleft()
        total -= x 

    if len(trucks) > 0 and total + trucks[-1] <= l:
        q.append(trucks[-1])
        total += trucks[-1]
        trucks.pop()

    else:
        q.append(0)
    t +=1 

print(t)
