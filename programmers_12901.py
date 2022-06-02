# 연습문제 - 2016년
# https://programmers.co.kr/learn/courses/30/lessons/12901

from datetime import datetime, timedelta
def solution(a, b):
    year=2016
    time_1 = datetime(year,1,1)
    time_2 = datetime(year,int(a),int(b))
    diff=time_2-time_1
    cnt=diff.days%7
    if cnt==0: answer = 'FRI'
    elif cnt==1: answer = 'SAT'
    elif cnt==2: answer = 'SUN'
    elif cnt==3: answer = 'MON'
    elif cnt==4: answer = 'TUE'
    elif cnt==5: answer = 'WED'
    elif cnt==6: answer = 'THU'
    return answer
