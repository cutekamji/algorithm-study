# 연습문제 - 자연수 뒤집어 배열로 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/12932

def solution(n):
    # 입력받은 정수를 문자타입으로 변환
    n_str = str(n)
    # 문자열 각각을 숫자형으로 변환하면서 리스트 원소로 받기
    n_list=[]
    for i in n_str:
        n_list.append(int(i))
    # 순서대로 입력받은 리스트를 역순으로 재배치
    answer = n_list[::-1]
    return answer
