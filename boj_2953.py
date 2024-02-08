import sys
sys.stdin=open("input.txt", "r")
from collections import deque
import heapq as hq
import itertools as it
import hashlib
import copy 


#백준_2953#

result = 0
max_value = 0 

for i in range(5):
    row = list(map(int,input().split()))
    summary = sum(row)

    if max_value < summary:
        max_value = summary
        result = i+1 

print(result, max_value)