# 2022 DGIST 현풍전산배 알고리즘 대회 Open Contest
# 1번. 에어컨
# https://www.acmicpc.net/problem/25044

from datetime import datetime
from datetime import timedelta

n, k = map(int, input().split())

def real_day(n,k):
    x=round((n*24*60)/(24*60+59))
    return x

# delay_day=(n*k)//(24*60) # 연기된 날짜 찾는 부분에서 고생
delay_day = real_day(n,k)
delay_time=(delay_day*k)%(24*60)

t1=datetime. strptime('15:00', '%H:%M')
t2=datetime. strptime('18:00', '%H:%M')
t3=datetime. strptime('21:00', '%H:%M')

if delay_time < 3*60:
    t1 = t1 + timedelta(minutes=delay_time)
    t2 = t2 + timedelta(minutes=delay_time)
    t3 = t3 + timedelta(minutes=delay_time)
elif 3*60<=delay_time and delay_time<6*60:
    t1 = t1 + timedelta(minutes=delay_time)
    t2 = t2 + timedelta(minutes=delay_time)
    t3 = t3 + timedelta(minutes=delay_time-k)
elif 6*60<=delay_time and delay_time<9*60:
    t1 = t1 + timedelta(minutes=delay_time)
    t2 = t2 + timedelta(minutes=delay_time-k)
    t3 = t3 + timedelta(minutes=delay_time-k)
else:
    t1 = t1 + timedelta(minutes=delay_time-k)
    t2 = t2 + timedelta(minutes=delay_time-k)
    t3 = t3 + timedelta(minutes=delay_time-k)
    
time_list = [t1.strftime('%H:%M'),t2.strftime('%H:%M'),t3.strftime('%H:%M')]
time_list.sort()

print(len(time_list))
for i in time_list:
    print(i)
