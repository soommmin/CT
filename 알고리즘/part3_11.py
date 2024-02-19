import sys
sys.stdin=open("input.txt", "r")
from collections import deque
import heapq as hq
import itertools as it
import hashlib
import copy 


# 격자판 회문수
board=[list(map(int, input().split())) for _ in range(7)]
cnt=0

for i in range(7):
    for j in range(3):
        tmp = board[i][j:j+5]
        if tmp == tmp[::-1]:
            cnt +=1 

        for k in range(2):
            if board[j+k][i] != board[j+5-k-1][i]:
                break 

        else:
            cnt +=1 

print(cnt)
