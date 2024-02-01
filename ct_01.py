import sys
sys.stdin=open("input.txt", "r")
from collections import deque
import heapq as hq
import itertools as it
import hashlib
import copy 


#백준_2920#


a = list(map(int,input().split(' ')))

ascending = True
descending = True 

for i in range(1, 8):
    if a[i] > a[i-1]:
        descending = False 

    elif a[i] < a[i-1]:
        ascending = False

if ascending:
    print('ascending')

elif descending:
    print("descending")

else:
    print("mixed")