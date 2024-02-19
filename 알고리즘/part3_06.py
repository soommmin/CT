import sys
sys.stdin=open("input.txt", "r")
from collections import deque
import heapq as hq
import itertools as it
import hashlib
import copy 


# 격자판 최대합

n = int(input())
a = [list(map(int,input().split())) for _ in range(5)]

maxx = 0 

for i in range(n):
    sum1 = sum2 = 0 
    for j in range(n):
        sum1 += a[i][j]
        sum2 += a[j][i]

    if sum1 > maxx:
        maxx = sum1 

    if sum2 > maxx:
        maxx = sum2 



sum1 = sum2 = 0 

for i in range(n):
    sum1 += a[i][i]
    sum2 += a[i][n-i-1]

if sum1 > maxx:
    maxx = sum1 

if sum2 > maxx:
    maxx = sum2 


print(maxx)