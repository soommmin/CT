import sys
sys.stdin=open("input.txt", "r")
from collections import deque
import heapq as hq
import itertools as it
import hashlib
import copy 


#백준_7662#

def pop(heap):
    while len(heap) > 0:
        data, id = hq.heappop(heap)
        if not deleted[id]:
            deleted[id] = True
            return data 
        
    return None 

for _ in range(int(input())):
    k = int(input())
    min_heap = []
    max_heap = []

    current = 0 
    deleted = [False] * (k+1)

    for i in range(k):
        command = input().split()
        operator, data = command[0], int(command[1])

        if operator == 'D':
            if data == -1:
                pop(min_heap)
            elif data == 1:
                pop(max_heap)
                
        elif operator == 'I':
            hq.heappush(min_heap, (data, current))
            hq.heappush(max_heap, (-data, current))
            current +=1 

    max_value = pop(max_heap)
    if max_value == None:
        print("EMPTY")
    else:
        hq.heappush(min_heap, (-max_value, current))
        print(-max_value, pop(min_heap))