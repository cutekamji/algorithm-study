# 피보나치 수 5
# https://www.acmicpc.net/problem/10870


# 내가 푼 풀이 - For문 사용
n=int(input())
# 숫자를 입력할 리스트
li = [0,1]
# 10번째 수가 나올때까지 반복
for i in range(2,n+1):
    num = li[i-2]+li[i-1]
    li.append(num)
# n번째 수 출력
print(li[n])


# 재귀함수 풀이
# 풀이 출처 - https://ooyoung.tistory.com/115
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

n = int(input())
print(fibonacci(n))
