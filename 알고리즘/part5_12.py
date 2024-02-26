import sys
sys.stdin=open("input.txt", "r")
from collections import deque
import heapq as hq
import itertools as it
import hashlib
import copy 


# 최대힙

a = []
while True:
    n = int(input())

    if n == -1:
        break

    if n == 0:
        if len(a) == 0:
            print(-1)

        else:
            print(-hq.heappop(a))

    else:
        hq.heappush(a, -n)