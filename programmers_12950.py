# 연습문제 - 행렬의 덧셈
# https://programmers.co.kr/learn/courses/30/lessons/12950

import numpy as np

def solution(arr1, arr2):
    # 리스트를 배열 형식으로 변환하여 연산
    arr_sum = np.array(arr1) + np.array(arr2)
    # 연산한 배열을 다시 리스트 형식으로 변환
    answer = arr_sum.tolist()
    return answer
