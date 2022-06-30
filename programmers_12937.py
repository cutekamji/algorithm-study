# 연습문제 - 짝수와 홀수
# https://programmers.co.kr/learn/courses/30/lessons/12937

def solution(num):
    # num이 짝수인 경우
    if num%2==0:
        answer = 'Even'
    # num이 홀수인 경우
    else:
        answer = 'Odd'
    return answer
