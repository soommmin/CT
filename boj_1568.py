import sys
sys.stdin=open("input.txt", "r")
from collections import deque
import heapq as hq
import itertools as it
import hashlib
import copy 


#백준_1568#

n = int(input())
result = 0

k = 1 

while n != 0:
    if k > n:
        k = 1 
    n -=1 
    k +=1 
    result +=1 


print(result)

