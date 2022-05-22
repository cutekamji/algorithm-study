# 해시 - 완주하지 못한 선수
# https://programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    participant.sort()
    completion.sort()
    if participant[:-1]==completion:
        answer=participant[-1]
    else:
        for i in range(0,len(participant)-1):
            if participant[i]!=completion[i]:
                answer=participant[i]
                break
            else: pass
    return answer
