import sys
sys.stdin=open("input.txt", "r")
from collections import deque
import heapq as hq
import itertools as it
import hashlib
import copy 


# 회의실 배정(그리디)

n = int(input())
room = []

for i in range(n):
    a,b = map(int,input().split())
    room.append((a,b))

room.sort(key=lambda x: (x[1], x[0]))
cnt = 0
et = 0
for x,y in room:
    if x>=et:
        cnt +=1 
        et = y 

print(cnt)