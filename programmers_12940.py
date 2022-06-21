# 연습문제 - 최대공약수와 최소공배수
# https://programmers.co.kr/learn/courses/30/lessons/12940

def solution(n, m):
    # i - 최대공약수
    # reversed(range())를 사용할 경우보다 range(step=-1)) 사용하는게 코드상으로 간결함
    for i in range(n,0,-1):
        if (m%(i)==0)&(n%(i)==0):
            break
    # m*j - 최소공배수
    # n,m 중 큰 수 기준으로 배수를 구하면서 그 수가 작은 수로 나누어 떨어지는지 확인
    j=1
    while True:
        if (m*j)%n==0:
            break
        j+=1
    answer=[i,m*j]
    return answer
