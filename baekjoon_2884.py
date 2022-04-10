# 알람 시계
# https://www.acmicpc.net/problem/2884

# h : 입력 시간(시)
# m : 입력 시간(분)

h, m = map(int, input().split())
print(h,':',m)
if m<45:
    if h==0:
        h+=23
    else:
        h-=1
    m+=15
else:
    m-=45
print(h, m, end=' ')
