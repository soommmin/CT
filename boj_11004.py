import sys
sys.stdin=open("input.txt", "r")
from collections import deque
import heapq as hq
import itertools as it
import hashlib
import copy 


#백준_11004#

n,k = map(int,input().split())
array = list(map(int,input().split()))

array.sort()

print(array[k-1])