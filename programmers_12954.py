# 연습문제 - x만큼 간격이 있는 n개의 숫자
# https://programmers.co.kr/learn/courses/30/lessons/12954

def solution(x, n):
    # 증가하는 숫자를 입력받을 리스트
    answer = []
    # n번 반복하여 등비수열 값 생성
    for i in range(n):
        answer.append(x*(i+1))
    return answer
