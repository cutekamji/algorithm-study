# 월간 코드 챌린지 시즌2 - 약수의 개수와 덧셈
# https://school.programmers.co.kr/learn/courses/30/lessons/77884?language=python3

def solution(left, right):
    # 약수의 개수가 짝수인 수와 홀수인 수를 담을 리스트 생성
    even_li = []
    odd_li = []
    # left부터 right까지 반복문 생성
    for i in range(left, right+1):
        # 약수의 개수를 확인하기 위한 int형 변수 생성
        cnt=0
        for j in range(1,i+1):
            if i%j==0:
                cnt+=1
        # 약수의 개수가 짝수일 경우 even_li에 숫자 추가
        if cnt%2==0:
            even_li.append(i)
        # 약수의 개수가 홀수일 경우 odd_li에 숫자 추가
        else:
            odd_li.append(i)
    # 약수의 개수가 짝수인 리스트의 합에서 홀수인 리스트의 합 빼기
    answer = sum(even_li)-sum(odd_li)
    return answer
