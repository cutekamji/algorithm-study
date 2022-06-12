# 찾아라 프로그래밍 마에스터 - 폰켓몬
# https://programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    # 뽑을 수 있는 최대 포켓몬 수 구하기(조건1)
    N = len(nums)
    pick_max = N//2
    # 중복 포켓몬 제거
    num_set = list(set(nums))
    # 가능한 조합 최대값(조건2)
    pick_mix = len(num_set)
    # 두 조건을 만족하는 최대 값
    if pick_max>=pick_mix:
        answer = pick_mix
    else:
        answer = pick_max
    return answer
