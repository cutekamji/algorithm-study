# 연습문제 - 하샤드 수
# https://school.programmers.co.kr/learn/courses/30/lessons/12947

def solution(x):
    # 각 자리의 수를 더해주기 위한 int형 변수
    div=0
    # 입력받은 숫자를 문자형으로 바꿔서 for문으로 각 자리의 숫자를 반환
    # 반환한 숫자는 div에 누적합
    for i in str(x):
        div+=int(i)
    # 압력받은 x값을 div로 나눴을때 나누어 떨어지는 경우 True, 아닐경우 False 반환
    if x%div==0:
        answer = True
    else:
        answer = False
    return answer
