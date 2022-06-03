# 연습문제 - 나누어 떨어지는 숫자 배열
# https://programmers.co.kr/learn/courses/30/lessons/12910

def solution(arr, divisor):
    answer = []
    for n in arr:
        if n%divisor==0:
            answer.append(n)
    answer.sort()
    if len(answer)<1:
        answer=[-1]
    return answer
