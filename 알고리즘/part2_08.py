import sys
sys.stdin=open("input.txt", "r")
from collections import deque
import heapq as hq
import itertools as it
import hashlib
import copy 



# 뒤집은 소수

def reverse(x):
    res = 0 
    while x>0:
        t = x%10
        res = res*10+int(t)
        x = x//10 

    return res

def isPrime(x):
    if x ==1:
        return False
    
    for i in range(2, x//2+1):
        if x%i == 0:
            return False 
        
    else:
        return True 
n = int(input())
a = list(map(int,input().split()))

for x in a:
    tmp = reverse(x)

    if isPrime(tmp):
        print(tmp, end = ' ')