# 평균은 넘겠지
# https://www.acmicpc.net/problem/4344

c = int(input())
for i in range(c):
    all = list(map(int, input().split()))
    avg = sum(all[1:])/all[0]
    cnt = 0
    for i in all[1:]:
        if i > avg:
            cnt+=1
    per = cnt/all[0]*100
    print(f'{per:.3f}%')
