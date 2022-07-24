# 2020 KAKAO BLIND RECRUITMENT - 문자열 압축
# https://school.programmers.co.kr/learn/courses/30/lessons/60057

# 내가 푼 풀이
import re
from collections import OrderedDict

def solution(s):
    for i in range(1,len(s)+1):
        if len(s)%i==0:
            li = re.findall('.'*i, s)
            print(i)
            print(li)
    return answer
 
# 정답지
https://velog.io/@shelly/2020-KAKAO-BLIND-RECRUITMENT-%EB%AC%B8%EC%9E%90%EC%97%B4%EC%95%95%EC%B6%95
