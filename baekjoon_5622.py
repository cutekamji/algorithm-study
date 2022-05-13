# 다이얼
# https://www.acmicpc.net/problem/5622

s=input()
cnt=0
for i in s:
    if i in ['A','B','C']: num=2
    elif i in ['D','E','F']: num=3
    elif i in ['G','H','I']: num=4
    elif i in ['J','K','L']: num=5
    elif i in ['M','N','O']: num=6
    elif i in ['P','Q','R','S']: num=7
    elif i in ['T','U','V']: num=8
    elif i in ['W','X','Y','Z']: num=9
    cnt+=(num-1)*1+2
print(cnt)
