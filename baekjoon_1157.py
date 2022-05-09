# 단어 공부
# https://www.acmicpc.net/problem/1157

s = input().upper()
set_list=list(set(s))
cnt_list=[]
for i in set_list:
    cnt=s.count(i)
    cnt_list.append(cnt)
if cnt_list.count(max(cnt_list))>1:
    print('?')
else:
    print(set_list[cnt_list.index(max(cnt_list))])
