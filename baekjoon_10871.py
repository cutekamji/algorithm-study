# X보다 작은 수
# https://www.acmicpc.net/problem/10871

n, x = map(int, input().split()) # int 형식으로 입력을 받음
a = list(map(int, input().split())) # 리스트 형식으로 입력을 받음
for i in a:
    if i<x:
        print(i, end=' ')
