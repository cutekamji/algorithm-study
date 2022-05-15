# 설탕 배달
# https://www.acmicpc.net/problem/2839

n=int(input())
y=0
while n>=0:
    if n%5==0:
        y+=n//5
        print(y)
        break
    n-=3
    y+=1
else:
    print(-1)
