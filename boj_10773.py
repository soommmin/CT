import sys
sys.stdin=open("input.txt", "r")
from collections import deque
import heapq as hq
import itertools as it
import hashlib
import copy 


#백준_10773#

k = int(input())
stack =[]

for _ in range(k):
    x = int(input())
    if x  == 0:
        stack.pop()

    else:
        stack.append(x)

print(sum(stack))