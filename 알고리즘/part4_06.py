import sys
sys.stdin=open("input.txt", "r")
from collections import deque
import heapq as hq
import itertools as it
import hashlib
import copy 


# 씨름 선수(그리디)

n = int(input())
body = []

for i in range(n):
    a,b = map(int,input().split())
    body.append((a,b))


body.sort(reverse=True)
largest = 0 
cnt = 0 

for x,y in body:
    if y>largest:
        largest = y 
        cnt +=1 

print(cnt)
