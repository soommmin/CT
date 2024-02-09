import sys
sys.stdin=open("input.txt", "r")
from collections import deque
import heapq as hq
import itertools as it
import hashlib
import copy 


#백준_10809#

arr = [-1]*26
data = input().strip()

for i in range(len(data)):
    index = ord(data[i]) - ord('a')
    if arr[index] == -1:
        arr[index] = i 

for x in arr:
    print(x, end = ' ')