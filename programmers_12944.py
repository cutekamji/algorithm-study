# 연습문제 - 평균 구하기
# https://programmers.co.kr/learn/courses/30/lessons/12944

def solution(arr):
    # 배열을 리스트 형식으로 변환
    # arr = arr.tolist() -> 이미 리스트 형식으로 input되는 것이었음(생략)
    # 리스트 원소들의 평균 계산
    answer = sum(arr)/len(arr)
    return answer
