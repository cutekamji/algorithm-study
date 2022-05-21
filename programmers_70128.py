# 월간 코드 챌린지 시즌1 - 내적
# https://programmers.co.kr/learn/courses/30/lessons/70128

def solution(a, b):
    dot_p=[]
    for (i, j) in zip(a,b):
        d_p=i*j
        dot_p.append(d_p)
    answer = sum(dot_p)
    return answer
