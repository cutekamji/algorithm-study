# Summer/Winter Coding(~2018) - 예산
# https://programmers.co.kr/learn/courses/30/lessons/12982

def solution(d, budget):
    d.sort()
    s=0
    answer=0
    for i in d:
        s+=i
        if s>budget: break
        answer+=1
    return answer
