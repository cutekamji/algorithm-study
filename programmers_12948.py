# 연습문제 - 핸드폰 번호 가리기
# https://programmers.co.kr/learn/courses/30/lessons/12948

def solution(phone_number):
    # 변경할 부분
    chg_part = phone_number[:-4]
    # 유지할 부분
    save_part = phone_number[-4:]
    answer = "*"*len(chg_part)+save_part
    return answer
