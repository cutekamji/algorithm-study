# 더하기 사이클
# https://www.acmicpc.net/problem/1110

n = int(input())
n_new = n
cnt=0
while True:
    a = n_new//10
    b = n_new%10
    n_new = b*10 + (a+b)%10
    cnt+=1
    if n_new==n:
        break
print(cnt)
