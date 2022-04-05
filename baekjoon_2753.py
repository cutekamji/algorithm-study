# 윤년 구하기
# https://www.acmicpc.net/problem/2753

x = int(input())

if (x%4==0 and x%100!=0) or (x%400==0):
    print(1)
else:
    print(0)
