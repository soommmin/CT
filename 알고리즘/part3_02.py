import sys
sys.stdin=open("input.txt", "r")
from collections import deque
import heapq as hq
import itertools as it
import hashlib
import copy 



# 숫자만 추출

a = input()
res = 0
for x in a:
    if x.isdecimal():
        res = res*10+int(x)

print(res)
cnt = 0 

for i in range(1, res+1):
    if res%i == 0:
        cnt +=1 

print(cnt)
    