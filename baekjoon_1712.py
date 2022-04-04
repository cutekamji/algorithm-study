# 손익분기점
# https://www.acmicpc.net/problem/1712

# 제출 코드
A,B,C = map(int,input().split())

if B>=C : 
    x=-1
else:
    x = A//(C-B)+1
print(x)
