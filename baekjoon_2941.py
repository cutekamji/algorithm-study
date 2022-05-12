# 크로아티아 알파벳
# https://www.acmicpc.net/problem/2941

s=input()
cro=['c=','c-','dz=','d-','lj','nj','s=','z=']
for i in cro:
    s=s.replace(i,'*')
print(len(s))
