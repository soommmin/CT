import sys
sys.stdin=open("input.txt", "r")
from collections import deque
import heapq as hq
import itertools as it
import hashlib
import copy 



# k번째 약수 

n,k = map(int,input().split())
cnt = 0

for i in range(1, n+1):
    if n%i == 0:
        cnt +=1 

    if cnt == k:
        print(i)
        break 

else:
    print(-1)
