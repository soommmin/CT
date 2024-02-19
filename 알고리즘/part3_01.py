import sys
sys.stdin=open("input.txt", "r")
from collections import deque
import heapq as hq
import itertools as it
import hashlib
import copy 



# 회문 문자열 검사

n = int(input())

for i in range(n):
    str = input()
    str = str.upper()

    if str == str[::-1]:
        print("#%d yes" %(i+1))
        

    else:
        print("#%d no" %(i+1))