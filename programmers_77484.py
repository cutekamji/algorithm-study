# 로또의 최고 순위와 최저 순위
# https://programmers.co.kr/learn/courses/30/lessons/77484

def solution(lottos, win_nums):
    cnt=0
    rand=0
    for n in lottos:
        if n != 0:
            if n in win_nums:
                cnt+=1
        else: rand+=1
    if cnt<2:
        rank_z=6
    else: rank_z=7-cnt
    if cnt+rand<2:
        rank_a=6
    else: rank_a=7-(cnt+rand)    
    answer = [rank_a,rank_z]
    return answer
