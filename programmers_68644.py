# 월간 코드 챌린지 시즌1 - 두 개 뽑아서 더하기
# https://programmers.co.kr/learn/courses/30/lessons/68644

def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        numbers_2=numbers.copy()
        numbers_2.pop(i)
        for j in range(len(numbers_2)):
            val=numbers[i]+numbers_2[j]
            answer.append(val)
    answer = set(answer)
    answer = list(answer)
    answer.sort()
    return answer
