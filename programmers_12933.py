# 연습문제 - 정수 내림차순으로 배치하기
# https://programmers.co.kr/learn/courses/30/lessons/12933

def solution(n):
    # int -> str
    n = str(n)
    # 높은 숫자 순서로 정렬
    # 내림차순을 위한 reverse=True 옵션 추가
    n_li = sorted(n, reverse=True)
    # 리스트 형식을 string 형식으로 합치기
    answer = ''.join(n_li)
    # str -> int
    answer = int(answer)
    return answer
