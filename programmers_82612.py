# 위클리 챌린지 - 부족한 금액 계산하기
# https://programmers.co.kr/learn/courses/30/lessons/82612

def solution(price, money, count):
    cost=0
    for i in range(1,count+1):
        cost+=price*i
    if money>=cost:
        answer=0
    else:
        answer=cost-money
    return answer
