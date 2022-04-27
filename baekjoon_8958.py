# OX퀴즈
# https://www.acmicpc.net/problem/8958

n=int(input())
for i in range(n):
    res=str(input())
    scr=0
    add=0
    for loc in range(len(res)):
        if res[loc]=='O':
            add+=1
            scr+=add
        elif res[loc]=='X':
            add=0
    print(scr)
