import sys
sys.stdin=open("input.txt", "r")
from collections import deque
import heapq as hq
import itertools as it
import hashlib
import copy 


#백준_1904#
n = int(input())
dp = [0]*1000001
dp[1] = 1 
dp[2] = 2 


for i in range(3, n+1):
    dp[i] = (dp[i-2] + dp[i-1]) % 15746

print(dp[n]) 
