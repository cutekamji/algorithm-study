# 그룹 단어 체커
# https://www.acmicpc.net/problem/1316

n=int(input())
cnt=0
for num in range(n):
    add=1
    s=input()
    for idx in range(len(s)-1):
        if s[idx]!=s[idx+1]:
            check = s[idx+1:]
            if check.count(s[idx]) > 0: add=0
    cnt+=add
print(cnt)
