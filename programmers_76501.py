# 월간 코드 챌린지 시즌2 - 음양 더하기
# https://programmers.co.kr/learn/courses/30/lessons/76501

# True, False 사용법
def solution(absolutes, signs):
    answer=0
    for i in range(len(absolutes)):
        if signs[i]:
            answer+=absolutes[i]
        else:
            answer-=absolutes[i]
    return answer