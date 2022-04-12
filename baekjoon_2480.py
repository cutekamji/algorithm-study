# 주사위 세개
# https://www.acmicpc.net/problem/2480

# a : 첫 번째 주사위
# b : 두 번째 주사위
# c : 세 번째 주사위

a,b,c = map(int, input().split())

if a==b and b==c:
    reward = 10000 + a*1000
elif (a==b and a!=c) or (a==c and a!=b):
    reward = 1000 + a*100
elif (b==c and a!=b):
    reward = 1000 + b*100
else:
    reward = max(a,b,c)*100
    
print(reward)
