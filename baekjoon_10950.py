# A+B - 3
# https://www.acmicpc.net/problem/10950

# num : 테스트 케이스 개수 T
# a, b : 더해지는 정수

num = int(input())

for i in range(num):
    a, b = map(int, input().split())
    print(a+b)
