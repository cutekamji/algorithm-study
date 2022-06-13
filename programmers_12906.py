# 연습문제 - 같은 숫자는 싫어
# https://programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr):
    answer = []
    for i in range(len(arr)):
        # 첫번쨰로 받은 원소를 무조건 리스트에 추가
        if i==0:
            answer.append(arr[i])
            pass
        # 직전 원소와 중복될 경우 스킵
        elif arr[i-1]==arr[i]:
            pass
        # 그 외의 경우는 리스트에 추가
        else:
            answer.append(arr[i])
    return answer
