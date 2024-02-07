import sys
sys.stdin=open("input.txt", "r")
from collections import deque
import heapq as hq
import itertools as it
import hashlib
import copy 


#백준_1874#

n = int(input())
stack = []
answer = []
current = 1 

for _ in range(n):
    x = int(input())
    while len(stack) == 0 or stack[-1] < x:
        stack.append(current)
        current +=1 
        answer.append('+')

    if stack[-1] == x:
        stack.pop()
        answer.append('-')

    else:
        answer = ['NO']
        break

for x in answer:
    print(x)
