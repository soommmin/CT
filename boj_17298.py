import sys
sys.stdin=open("input.txt", "r")
from collections import deque
import heapq as hq
import itertools as it
import hashlib
import copy 


#백준_17298#

n = int(input())

arr = list(map(int,input().split()))
stack = []
NGE = [-1]*n 

for i in range(n):
    x = arr[i]

    if len(stack) == 0 or stack[-1][0] >= x:
        stack.append((x,i))

    else:
        while len(stack) > 0:
            prev, index = stack.pop()
            if prev >= x:
                stack.append((prev, index))
                break
            else:
                NGE[index] = x 
        stack.append((x,i))

for x in NGE:
    print(x, end = ' ')