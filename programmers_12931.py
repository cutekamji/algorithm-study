# 연습문제 - 자릿수 더하기
# https://programmers.co.kr/learn/courses/30/lessons/12931

def solution(n):
    # 각 자리의 숫자를 더하기 위한 변수
    answer=0
    while n>=10:
        # n을 10으로 나눈 나머지 누적합
        m=n%10
        answer+=m
        # n을 10으로 나눈 몫으로 값 갱신
        n=n//10
    # 마지막 남은 자릿수 더하기
    answer+=n%10
    return answer
