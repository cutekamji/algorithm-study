# 정렬 - K번째수
# https://programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    answer = []
    for command in commands:
        array_s=array.copy()
        array_s=array_s[command[0]-1:command[1]]
        array_s.sort()
        answer.append(array_s[command[2]-1])
    return answer
