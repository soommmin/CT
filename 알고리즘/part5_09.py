import sys
sys.stdin=open("input.txt", "r")
from collections import deque
import heapq as hq
import itertools as it
import hashlib
import copy 

# 아나그램(딕셔너리)

a=input()
b=input()
sH=dict()
for x in a:
    sH[x]=sH.get(x, 0)+1
for x in b:
    sH[x]=sH.get(x, 0)-1

for x in a:
    if(sH.get(x)>0):
        print("NO")
        break;
else:
    print("YES")

