# 팩토리얼
# https://www.acmicpc.net/problem/10872

n=int(input())
answer=1
# 1부터 n까지 누적곱(=팩토리얼)
for i in range(1,n+1):
    answer*=i
print(answer)
