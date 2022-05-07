# 문자열 반복
# https://www.acmicpc.net/problem/2675

n=int(input())
for i in range(n):
    num, s = input().split() # 서로 type이 달라 map 사용x
    num = int(num)
    s = str(s)
    for i in range(len(s)):
        print(s[i]*num, end='')
    print(end='\n') # 줄바꿈 용도
