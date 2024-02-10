import sys
sys.stdin=open("input.txt", "r")
from collections import deque
import heapq as hq
import itertools as it
import hashlib
import copy 


#백준_10989#

n = int(input())

array = []

for i in range(n):
    data = int(input())
    array.append(data)


array.sort()

for x in array:
    print(x)