import sys
sys.stdin=open("input.txt", "r")
from collections import deque
import heapq as hq
import itertools as it
import hashlib
import copy 


#백준_11053#
n = int(input())
array = list(map(int,input().split()))
dp = [1] * n 

for i in range(1, n):
    for j in range(0,i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] +1)

print(max(dp))
