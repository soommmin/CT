import sys
sys.stdin=open("input.txt", "r")
from collections import deque
import heapq as hq
import itertools as it
import hashlib
import copy 


#백준_2747#
n = int(input())

a,b = 0,1 

while n > 0:
    a,b = b, a + b 
    n -=1 

print(a)