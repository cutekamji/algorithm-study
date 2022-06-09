# 완전탐색 - 모의고사
# https://programmers.co.kr/learn/courses/30/lessons/42840

import numpy

def solution(answers):
    # 각 수포자별 답안 패턴 리스트로 입력
    a_1 = [1,2,3,4,5]
    a_2 = [2,1,2,3,2,4,2,5]
    a_3 = [3,3,1,1,2,2,4,4,5,5]
    # 수포자별 점수 변수(int형)
    sum_1 = 0
    sum_2 = 0
    sum_3 = 0
    # 입력된 답안 순설대로 채점
    # 주의 - elif를 사용할 경우 앞쪽 수포자가 정답일 경우 뒤쪽 수포자 정답은 무시됨
    for i in range(len(answers)):
        if answers[i]==a_1[i%len(a_1)]:
            sum_1+=1
        if answers[i]==a_2[i%len(a_2)]:
            sum_2+=1
        if answers[i]==a_3[i%len(a_3)]:
            sum_3+=1
            
    # 세 수포자 점수 리스트화(중복 없을 경우)
    # p_list = [sum_1, sum_2, sum_3]
    # answer = p_list.index(max(p_list))+1
    
    # 세 수포자 점수 리스트화(중복 있을 경우)
    p_list = [sum_1, sum_2, sum_3]
    max_val = max(p_list)
    p_arr = numpy.array(p_list)
    answer = numpy.where(p_arr == max_val)[0].tolist()
    # 인덱스는 0부터 시작하므로 각 원소에 1씩 더해줌
    for i in range(len(answer)):
        answer[i]+=1
    return answer
