# 연습문제 - 문자열 내 p와 y의 개수
# https://programmers.co.kr/learn/courses/30/lessons/12916

def solution(s):
    # 입력값 모두 소문자로 변환
    s=s.lower()
    # p, y값을 카운트할 변수 생성(int형)
    p_cnt = 0
    y_cnt = 0
    # 문자 자리수의 값이 p 혹은 y인지 확인
    for i in s:
        # i가 p이면 p_cnt에 1 더하기
        if i=='p':
            p_cnt+=1
        # i가 y이면 p_cnt에 1 더하기
        elif i=='y':
            y_cnt+=1
    # p, y 개수 비교
    # 개수 같으면 True, 다르면 False 리턴
    if p_cnt==y_cnt:
        answer = True
    else: 
        answer = False
    return answer
