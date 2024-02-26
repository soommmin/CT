import sys
sys.stdin=open("input.txt", "r")
from collections import deque
import heapq as hq
import itertools as it
import hashlib
import copy 

# 단어 찾기

n = int(input())
p = dict()

for i in range(n):
    word = input()
    p[word] = 1 

for i in range(n-1):
    word = input()
    p[word] = 0 

for key, val in p.items():
    if val == 1:
        print(key)
        break