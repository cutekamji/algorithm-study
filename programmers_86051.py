# 월간 코드 챌린지 시즌3
# 없는 숫자 더하기
# https://programmers.co.kr/learn/courses/30/lessons/86051

def solution(numbers):
    a_li=[0,1,2,3,4,5,6,7,8,9]
    for num in numbers:
        a_li.remove(num)
    answer=sum(a_li)
    return answer
