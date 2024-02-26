import sys
sys.stdin=open("input.txt", "r")
from collections import deque
import heapq as hq
import itertools as it
import hashlib
import copy 


# 교육과정 설계

need = input()
n = int(input())
for i in range(n):
    plan = input()
    dq = deque(need)
    for x in plan:
        if x in dq:
            if x != dq.popleft():
                print("#%d no" %(i+1))
                break


    else:
        if len(dq) == 0:
            print("#%d yes" %(i+1))

        else:
            print("#%d no" %(i+1))