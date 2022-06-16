# 연습문제 - 정수 제곱근 판별
# https://programmers.co.kr/learn/courses/30/lessons/12934

def solution(n):
    # 정수 1부터 제곱을 구해서 n값이 되는 정수를 구함
    # 정수형 숫자 타입 변수 생성
    i=1
    # i의 제곱이 n 이상이 될 때의 i값을 구하기 위한 loop문
    while i**2 < n:
        i+=1
    # i의 제곱이 n과 동일하면 (i+1)의 제곱값, 아니면 -1을 answer로 반환
    if i**2==n:
        answer = (i+1)**2
    else:
        answer = -1
    return answer
