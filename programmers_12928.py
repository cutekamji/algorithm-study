# 연습문제 - 약수의 합
# https://programmers.co.kr/learn/courses/30/lessons/12928

def solution(n):
    # n의 약수를 입력받을 리스트
    n_list = []
    # n을 1부터 n까지 나눴을 떄 나머지가 0인 경우 리스트에 append
    for i in range(1,n+1):
        if n%i==0:
            n_list.append(i)
    # n의 약수를 담은 리스트 원소들의 합 반환
    answer = sum(n_list)
    return answer
