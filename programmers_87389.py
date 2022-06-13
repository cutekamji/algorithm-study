# 월간 코드 챌린지 시즌3 - 나머지가 1이 되는 수 찾기
# https://programmers.co.kr/learn/courses/30/lessons/87389

def solution(n):
    # n-1의 약수 구하기
    m=n-1
    # n-1의 약수를 담을 리스트
    li=[]
    # 2부터 n-1까지의 범위 조회
    for i in range(2,n):
        if m%i==0:
            li.append(i)
    # n-1의 약수들 중 가장 작은 값 반환
    answer = min(li)
    return answer
