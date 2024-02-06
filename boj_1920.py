import sys
sys.stdin=open("input.txt", "r")
from collections import deque
import heapq as hq
import itertools as it
import hashlib
import copy 


#백준_1920#

n = int(input())
array = set(map(int, input().split()))
m = int(input())
x = list(map(int,input().split()))


for i in x:
    if i not in array:
        print('0')

    else:
        print('1')