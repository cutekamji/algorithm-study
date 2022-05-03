# 한수
# https://www.acmicpc.net/problem/1065

n = int(input())
if n<100:
    result=n
else:
    add=0
    for number in range(100,n+1):
        num_list = list(map(int, str(number)))
        if num_list[0]-num_list[1]==num_list[1]-num_list[2]:
            add+=1
    result=99+add
print(result)
