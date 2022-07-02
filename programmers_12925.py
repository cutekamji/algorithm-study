# 연습문제 - 문자열을 정수로 바꾸기
# https://programmers.co.kr/learn/courses/30/lessons/12925

def solution(s):
    # - 부호가 있는 경우
    if s[0]=='-':
        answer = int(s[1:]) * (-1)
    # - 부호가 없는 경우
    else:
        answer = int(s)
    return answer
