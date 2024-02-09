import sys
sys.stdin=open("input.txt", "r")
from collections import deque
import heapq as hq
import itertools as it
import hashlib
import copy 


#백준_1374#

n = int(input())
lectures = []
for i in range(n):
    id, start, end  = map(int,input().split())
    hq.heappush(lectures, (start, end))


heap = []
end = hq.heappop(lectures)[1]
hq.heappush(heap, end)
answer = 1 

for i in range(n-1):
    new_start, new_end = hq.heappop(lectures)
    end = hq.heappop(heap)

    if new_start < end:
        hq.heappush(heap, end)
        hq.heappush(heap, new_end)
        answer +=1 

    else:
        hq.heappush(heap, new_end)

print(answer)