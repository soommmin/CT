import sys
sys.stdin=open("input.txt", "r")
from collections import deque
import heapq as hq
import itertools as it
import hashlib
import copy 


#백준_11650#

n = int(input())

array = []

for _ in range(n):
    x,y = map(int,input().split())
    array.append((x,y))

array.sort()

for x in array:
    print(x[0], x[1])