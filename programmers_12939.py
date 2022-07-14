# 연습문제 - 최댓값과 최솟값
# https://school.programmers.co.kr/learn/courses/30/lessons/12939

def solution(s):
    # 문자열 공백 기준으로 분리
    s_li = s.split(' ')
    int_li = []
    for s in s_li:
        # 문자를 정수형으로 변환
        s_int = int(s)
        int_li.append(s_int)
    answer = f"{min(int_li)} {max(int_li)}"
    return answer
