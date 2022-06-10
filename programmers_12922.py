# 연습문제 - 수박수박수박수박수박수?
# https://programmers.co.kr/learn/courses/30/lessons/12922

def solution(n):
    # 수박..을 누적해서 입력할 리스트
    answer_li=[]
    for i in range(n):
        # 홀수번째 자리에 '수' 입력
        if i%2==0:
            answer_li.append('수')
        # 짝수번째 자리에 '박' 입력
        else:
            answer_li.append('박')
    # 리스트를 합쳐서 문자열로 반환
    answer = ''.join(answer_li)
    return answer
