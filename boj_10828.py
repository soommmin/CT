import sys
sys.stdin=open("input.txt", "r")
from collections import deque
import heapq as hq
import itertools as it
import hashlib
import copy 


#백준_10828#

n = int(input())
stack = []

for _ in range(n):
    command = input().strip().split(' ')
    if command[0] == 'push':
        stack.append(int(command[1]))

    elif command[0] == 'pop':
        if len(stack) == 0: print(-1)
        else: print(stack.pop())

    elif command[0] == 'size':
        print(len(stack))

    elif command[0] == 'empty':
        if len(stack) == 0: print(1)
        else: print(0) 

    elif command[0] == 'top':
        if len(stack) == 0: print(-1)
        else: print(stack[-1])