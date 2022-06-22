# 연습문제 - 콜라츠 추측
# https://programmers.co.kr/learn/courses/30/lessons/12943

def solution(num):
    # 반복 횟수 제한을 위한 변수(int형)
    cnt=0
    # num이 1이 될때까지 아래의 과정 반복
    while num>1:
        # 입력된 수가 짝수일 경우
        if num%2==0:
            num = num//2
        # 입력된 수가 홀수일 경우
        else:
            num = num*3+1
        cnt+=1
        # 작업 수가 500번에 도달하면 중단하고 -1 반환
        if cnt == 500:
            cnt = -1
            break
    return cnt
