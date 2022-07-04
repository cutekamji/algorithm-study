# 연습문제 - 문자열 내림차순으로 배치하기
# https://programmers.co.kr/learn/courses/30/lessons/12917

def solution(s):
    # 입력받은 문자를 하나씩 아스키코드로 변환 후 리스트에 추가
    n_li = []
    for i in range(len(s)):
        j = ord(s[i])
        n_li.append(j)
    # 리스트 내림차순 정렬
    n_li.sort(reverse=True)
    # 리스트의 원소를 문자로 변환하여 합치기
    answer=''
    for j in n_li:
        answer+=chr(j)
    return answer
