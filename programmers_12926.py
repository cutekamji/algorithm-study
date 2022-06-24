# 연습문제 - 시저 암호
# https://programmers.co.kr/learn/courses/30/lessons/12926

def solution(s, n):
    answer = ''
    for i in range(len(s)):
        # i번째 문자가 공백일 경우
        # 별 다른 처리없이 공백으로 입력
        if s[i]==' ':
            answer+=s[i]           
        # i번째 문자가 대문자일 경우
        elif s[i].isupper()==True:
            # i번째 문자 아스키코드에 n만큼 밀었을 때 'Z' 이후로 넘어가는 경우
            # ord : 문자 -> 아스키코드
            # chr : 아스키코드 -> 문자
            if ord(s[i])+n>ord('Z'):
                answer+=chr(ord('A')+(n-(ord('Z')-ord(s[i])+1)))
            # i번째 문자 아스키코드에 n만큼 밀었을 때 'Z' 이후로 넘지않는 경우
            else:
                answer+=chr(ord(s[i])+n)
        # i번째 문자가 소문자일 경우
        elif s[i].islower()==True:
            # i번째 문자 아스키코드에 n만큼 밀었을 때 'z' 이후로 넘어가는 경우
            if ord(s[i])+n>ord('z'):
                answer+=chr(ord('a')+(n-(ord('z')-ord(s[i])+1)))
            # i번째 문자 아스키코드에 n만큼 밀었을 때 'z' 이후로 넘지않는 경우
            else:
                answer+=chr(ord(s[i])+n)
    return answer
