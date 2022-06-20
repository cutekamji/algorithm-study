# 연습문제 - 이상한 문자 만들기
# https://programmers.co.kr/learn/courses/30/lessons/12930

def solution(s):
    # 우선 입력받은 문자 모두 소문자로 변환
    s = s.lower()
    # 공백 기준으로 문자열 분리
    s_li = s.split(' ')
    # 추후 대문자 변환한 문자열 입력받을 리스트 생성
    answer_part = []
    # 공백 기준 문자열 전용 반복문
    for i in range(len(s_li)):
        # 각 문자열 내에서 대문자 변환 진행한 알파벳 입력받을 리스트 생성
        s_li_2 = []
        # 각 문자열 내 알파벳 위치 전용 반복문
        for j in range(len(s_li[i])):
            # 각 리스트 원소 중 홀수번째인 경우 대문자로 변환
            # upper 함수를 거쳐 변환된 문자열을 리스트 원소로 할당하고자 했으나 불가능하여 기존에 생성했던 빈 리스트에 append
            if j%2==0:
                s_li_2.append(s_li[i][j].upper())
            else:
                s_li_2.append(s_li[i][j])
        # 각 문자열을 위한 변환된 알파벳 리스트는 공백 없이 조인
        answer_part.append(''.join(s_li_2))
    # 리스트 원소 다시 공백 추가하여 합치기
    answer = ' '.join(answer_part)
    return answer
