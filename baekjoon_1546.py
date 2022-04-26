# 평균
# https://www.acmicpc.net/problem/1546

n=int(input())
scr_list=list(map(int,input().split()))
max_scr=max(scr_list)
sum=0
for i in range(n):
    sum+=scr_list[i]/max_scr*100
print(sum/n)
