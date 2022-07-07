# 연습문제 - 문자열 다루기 기본
# https://school.programmers.co.kr/learn/courses/30/lessons/12918

def solution(s):
    answer = True
    # 조건1. 길이가 4 혹은 6
    # s의 길이가 4, 6이 아닐경우 False 반환
    if len(s) not in [4,6]:
        answer = False
    # 조건2. 숫자로만 구성
    # 문자(s) 하나씩 int형 변환 시도
    # 숫자형이 아니면 int변환에서 에러가 발생하면서 False 반환
    for i in s:
        try: i = int(i)
        except: 
            answer = False
            break
    return answer
