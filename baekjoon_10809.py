# 알파벳 찾기
# https://www.acmicpc.net/problem/10809

s=input()
alphabet='abcdefghijklmnopqrstuvwxyz'
for i in range(len(alphabet)):
    loc=s.find(alphabet[i])
    print(loc, end=' ')
