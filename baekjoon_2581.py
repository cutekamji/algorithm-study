# 소수
# https://www.acmicpc.net/problem/2581

m = int(input())
n = int(input())
# 소수인 수들을 저장할 리스트
li = []
# m부터 n까지 반복
for num in range(m, n+1):
    # 소수 확인을 위한 변수
    error = 0
    if num > 1 : # 이 조건이 없으면 오답으로 인식
        for i in range(2, num):
            # 소수일 경우 error에 1을 더해줌 -> 추후 error값이 0보다 클 경우 소수 리스트에 append
            if num % i == 0:
                error += 1
                break 
        if error == 0:
            li.append(num) 

if len(li) > 0 :
    print(sum(li))
    print(min(li))
else:
    print(-1)
