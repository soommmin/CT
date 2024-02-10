import sys
sys.stdin=open("input.txt", "r")
from collections import deque
import heapq as hq
import itertools as it
import hashlib
import copy 


#백준_1427#

n = int(input())
list = []

for i in str(n):
    list.append(int(i))


list.sort(reverse=True)

for x in list:
    print(x, end = '')