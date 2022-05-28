# 연습문제 - 가운데 글자 가져오기
# https://programmers.co.kr/learn/courses/30/lessons/12903

def solution(s):
    if len(s)%2==0: # 짝수
        strt=(len(s)-2)//2
        answer=s[strt:strt+2]
    else: # 홀수
        strt=len(s)//2
        answer = s[strt]
    return answer
