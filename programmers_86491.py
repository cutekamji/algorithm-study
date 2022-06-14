# 위클리 챌린지 - 최소직사각형
# https://programmers.co.kr/learn/courses/30/lessons/86491

def solution(sizes):
    # 꼭 가로 세로 방향 맞춰서 넣는다는 말은 없음(가로 세로 고려하지 않음)
    # 각 명항별 더 짧은 쪽 길이, 더 긴쪽의 길이를 분류해서 리스트화
    max_li=[]
    min_li=[]
    for i in sizes:
        max_li.append(max(i))
        min_li.append(min(i))
    # 각 리스트에서 가장 큰 값끼리 곱하기
    answer = max(max_li)*max(min_li)
    return answer
