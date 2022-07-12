# 연습문제 - 문자열 내 마음대로 정렬하기
# https://school.programmers.co.kr/learn/courses/30/lessons/12915

def solution(strings, n):
    db=dict()
    # 딕셔너리 틀 생성
    for str in strings:
        db[str[n]]=[]
    # n번째 문자를 키값으로 하고 해당되는 단어를 리스트 형식으로 추가
    for str in strings:
        db[str[n]].append(str) 
    answer=[]
    # 딕셔너리 키 값을 정렬
    # 순서대로 키-값 조회
    li=list(db.keys())
    li.sort()
    for i in li:
        # 만약 해당 값이 1개 이상일 경우 리스트 정렬
        if len(db[i])>1:
            db[i].sort()
        answer+=db[i]
    return answer
