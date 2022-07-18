# 소인수분해
# https://www.acmicpc.net/problem/11653

n=int(input())
i=2
# 몫이 1이되면 반복 중지
while n>1:
    # 나눠지지 않을때까지 출력 반복
    while n%i==0:
        n=n//i
        print(i)
    # 나누어떨어지지 않으면 인수 1씩 늘려서 반복
    else:
        i+=1
