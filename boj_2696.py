import sys
sys.stdin=open("input.txt", "r")
from collections import deque
import heapq as hq
import itertools as it
import hashlib
import copy 


#백준_2696#

def show_result():
    print(len(result))
    for i in range(len(result)):
        print(result[i], end = ' ')
        if (i+1) % 10 == 0:
            print()
    print()


for _ in range(int(input())):
    m = int(input())
    data = []
    for i in range(m // 10+1):
        data.extend(list(map(int,input().split())))

    left = []
    right = []
    median = data[0]
    result = [median]

    for i in range(1, m):
        if data[i] <= median:
            hq.heappush(left, -data[i])
        else:
            hq.heappush(right, data[i])
        
        if i % 2 == 0:
            if len(left) > len(right):
                hq.heappush(right, median)
                median = -hq.heappop(left)
            elif len(left) < len(right):
                hq.heappush(left, -median)
                median = hq.heappop(right)
            result.append(median)

    show_result()