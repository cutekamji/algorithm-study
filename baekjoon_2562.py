# 최댓값
# https://www.acmicpc.net/problem/2562

import sys

li=[]

for i in range(9):
    n = int(sys.stdin.readline())
    li.append(n)
print(max(li))
print(li.index(max(li))+1)
