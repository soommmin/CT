import sys
sys.stdin=open("input.txt", "r")
from collections import deque
import heapq as hq
import itertools as it
import hashlib
import copy 


#백준_1874#



n = int(input())

count = 1 
stack = []
result = []

for i in range(1, n+1):
    data = int(input())
    while count <= data:
        stack.append(count)
        count+=1 
        result.append('+')

    if stack[-1] == data:
        stack.pop()
        result.append('-')

    else:
        print('no')
        exit(0)

for x in result:
    print(x)