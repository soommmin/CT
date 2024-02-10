import sys
sys.stdin=open("input.txt", "r")
from collections import deque
import heapq as hq
import itertools as it
import hashlib
import copy 


#백준_10814#

n = int(input())

array = []

for _ in range(n):
    input_data = input().split()
    array.append((int(input_data[0]), input_data[1]))

array.sort(key= lambda x: x[0])

for x in array:
    print(x[0], x[1])