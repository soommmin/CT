import sys
sys.stdin=open("input.txt", "r")
from collections import deque
import heapq as hq
import itertools as it
import hashlib
import copy 


#백준_2798#

n,m = list(map(int,input().split(' ')))
data = list(map(int,input().split(' ')))


result = 0 
length = len(data)

count = 0 


for i in range(0, length):
    for j in range(i+1, length):
        for k in range(j+1, length):
            sum_value = data[i]+data[j]+data[k] 

            if sum_value <= m:
                result = max(result, sum_value)

print(result)