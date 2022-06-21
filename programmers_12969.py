# 연습문제 - 직사각형 별찍기
# https://programmers.co.kr/learn/courses/30/lessons/12969

n, m = map(int, input().strip().split(' '))
# n - 가로 길이
# m - 세로 길이
# 세로 길이만큼 print문 반복
for i in range(m):
    # 한 줄에 *을 가로 길이만큼 print
    print("*"*n)
