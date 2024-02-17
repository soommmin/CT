import sys
sys.stdin=open("input.txt", "r")
from collections import deque
import heapq as hq
import itertools as it
import hashlib
import copy 



# 주사위 게임

n = int(input())
max = -2147000000

for i in range(n):
    tmp = list(map(int,input().split()))
    tmp.sort()
    a,b,c = map(int, tmp)

    if a==b and b==c:
        money = 10000+(a*1000)

    elif a==b or a==c:
        money = 1000+(a*100)

    elif b==c:
        money = 1000+(b*100)

    else:
        money = 1000+(c*100)


    if money > max:
        max = money 

print(max)
