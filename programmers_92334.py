# 2022 KAKAO BLIND RECRUITMENT - 신고 결과 받기
# https://school.programmers.co.kr/learn/courses/30/lessons/92334

def solution(id_list, report, k):
    # 조건 - 동일한 유저에 대한 신고 횟수는 1회로 처리
    report = list(set(report))
    # 신고 내용 정보를 담기위한 딕셔너리
    db=dict()
    # 메일 대상자 카운트를 위한 딕셔너리
    answer_db=dict()
    # 유저 목록에 맞게 딕셔너리 형식 지정
    for id in id_list:
        db[id]=dict()
        db[id]['cnt']=0
        db[id]['report']=[]
        answer_db[id]=0
    # 신고 목록별 사용자의 누적 신고 횟수와 신고자 기록
    for case in report:
        user=case.split(' ')[0]
        rep=case.split(' ')[1]
        db[rep]['cnt']+=1
        db[rep]['report'].append(user)
    # 신고 횟수가 k번 이상일 경우 신고자 기준으로 메일 전달 횟수 더하기
    for id in id_list:
        if db[id]['cnt']>=k:
            for j in db[id]['report']:
                answer_db[j]+=1
    # 메일 전달 횟수 입력용 리스트
    answer=[]
    for id in id_list:
        answer.append(answer_db[id])
    return answer
