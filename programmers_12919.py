# 연습문제 - 서울에서 김서방 찾기
# https://programmers.co.kr/learn/courses/30/lessons/12919?language=python3

def solution(seoul):
    # 리스트에서 "Kim" 원소의 리스트 반환
    loc=seoul.index("Kim")
    answer = f'김서방은 {loc}에 있다'
    return answer
