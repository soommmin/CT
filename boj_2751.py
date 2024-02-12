import sys
sys.stdin=open("input.txt", "r")
from collections import deque
import heapq as hq
import itertools as it
import hashlib
import copy 


#백준_2751#

n = int(input())
array = []

for _ in range(n):
    array.append(int(input()))


array.sort()

for x in array:
    print(x)