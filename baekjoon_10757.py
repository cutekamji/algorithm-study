# 큰 수 A+B
# https://www.acmicpc.net/problem/10757

a,b = map(int, input().split())
print(a+b)

# 검색해보니 이 문제는 위의 방식대로 풀면 메모리가 터지는데 Python은 overflow가 없기 때문에 터지지 않음
# 그래도 아래 코드와 같이 sys 모듈을 지정하고 input을 주는 것이 정석
import sys
input=sys.stdin.readline
a,b = map(int, input().split())
print(a+b)
