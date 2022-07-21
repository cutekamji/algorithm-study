# 구간 합 구하기 4
# https://www.acmicpc.net/problem/11659

import sys
input=sys.stdin.readline
n, m = map(int, input().split())
li = list(map(int, input().split()))
# 리스트를 처음에 누적합 계산하며 읽어두기
for num in range(n-1):
    li[num+1]+=li[num]
# 인덱스 범위 맞춰주기
li = [0]+li
# m번 반복하여 출력
for _ in range(m):
    i, j = map(int, input().split())
    print(li[j]-li[i-1])
