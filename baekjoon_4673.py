# 셀프 넘버
# https://www.acmicpc.net/problem/4673

a_num=set(range(1,10000))
r_num=set()
for num in a_num:
    for n in str(num):
        num+=int(n)
    r_num.add(num)
s_num = a_num - r_num
for s_n in sorted(s_num):
    print(s_n)
