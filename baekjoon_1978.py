# 소수 찾기
# https://www.acmicpc.net/problem/1978

n=int(input())
li=list(map(int, input().split()))
answer=0
for num in li:
    cnt=0
    if num>1:
        for i in range(2,num):
            if num%i==0:
                cnt+=1
        if cnt==0:
            answer+=1
print(answer)
