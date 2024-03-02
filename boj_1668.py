import sys
sys.stdin=open("input.txt", "r")
from collections import deque
import heapq as hq
import itertools as it
import hashlib
import copy 


#백준_1668#

def ascending(array):
    now = array[0]
    result = 1 
    for i in range(1, len(array)):
        if now < array[i]:
            result +=1 
            now = array[i]
    return result 



n = int(input())
array = []

for _ in range(n):
    array.append(int(input()))


print(ascending(array))
array.reverse()
print(ascending(array))