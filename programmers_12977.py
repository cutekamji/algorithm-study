# Summer/Winter Coding(~2018) - 소수 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/12977

from itertools import combinations

def solution(nums):
    # 리스트 원소 중 3개의 조합으로 이루어진 리스트
    comb_li = list(combinations(nums,3))
    # 소수가 아닌 숫자를 담을 리스트
    diff=[]
    # 콤비네이션 조합 반복하면서 숫자의 합이 소수인지 확인
    for comb in comb_li:
        sum_num = sum(comb)
        for i in range(2,sum_num):
            if sum_num%i==0:
                diff.append(sum_num)
                break
    # 전체 조합의 수에서 합이 소수가 아닌경우의 수를 빼줌
    answer = len(comb_li) - len(diff)
    return answer
