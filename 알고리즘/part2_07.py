import sys
sys.stdin=open("input.txt", "r")
from collections import deque
import heapq as hq
import itertools as it
import hashlib
import copy 



# 소수(에라토스테네스 체) 

n = int(input())
ch = [0]*(n+1)

cnt = 0 

for i in range(2, n+1):
    if ch[i] == 0:
        cnt +=1 

        for j in range(i, n+1, i):
            ch[j] = 1 

print(cnt)