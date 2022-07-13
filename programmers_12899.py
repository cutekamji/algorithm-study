# 연습문제 - 124 나라의 숫자
# https://school.programmers.co.kr/learn/courses/30/lessons/12899

def solution(n):
    a=[]
    # 반복문 설정
    while n>0:
        a.append(str((n-1)%3+1))
        n=(n-1)//3
    # 반복문 돌면서 리스트에 추가된 원소 순서 뒤집기
    a=a[::-1]
    b=''.join(a)
    # 124의 나라이므로 3 대신 4로 치환
    b=b.replace('3','4')
    # b=int(b)
    return b
