import sys
sys.stdin=open("input.txt", "r")
from collections import deque
import heapq as hq
import itertools as it
import hashlib
import copy 



# 점수계산 

n = int(input())
a = list(map(int,input().split()))

cnt = 0 
sum = 0 


for x in a:
    if x == 1:
        cnt +=1 
        sum += cnt 

    else:
        cnt = 0 

print(sum)