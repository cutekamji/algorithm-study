# 연습문제 - 제일 작은 수 제거하기
# https://programmers.co.kr/learn/courses/30/lessons/12935

def solution(arr):
    # 만약 arr의 원소가 하나인 경우 [-1] 반환
    if len(arr)==1:
        answer = [-1]
    else:
        # arr 중 가장 작은 수 도출
        m = min(arr)
        # arr에서 가장 작은 수가 위치하는 인덱스 구하기
        idx=arr.index(m)
        # 해당 인덱스 원소 제거
        del arr[idx]
        answer=arr
    return answer
