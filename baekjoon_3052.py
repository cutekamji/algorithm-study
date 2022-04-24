# 나머지
# https://www.acmicpc.net/problem/3052

# 접근 : 리스트 중복 제거
n = []
for i in range(10):
    n.append(int(input())%42)
res = set(n)
print(len(res))
