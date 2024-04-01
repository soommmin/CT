import sys
sys.stdin=open("input.txt", "r")
from collections import deque
import heapq as hq
import itertools as it
import hashlib
import copy 


#백준_1715#

n = int(input())
heap = []

for i in range(n):
    data = int(input())
    hq.heappush(heap, data)

result = 0 

while len(heap) != 1:
    one = hq.heappop(heap)
    two = hq.heappop(heap)
    sum_value = one+ two 
    result += sum_value
    hq.heappush(heap, sum_value)

print(result)