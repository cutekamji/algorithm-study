# 신규 아이디 추천
# 2021 KAKAO BLIND RECRUITMENT
# https://programmers.co.kr/learn/courses/30/lessons/72410

import re

def solution(new_id):
    # STEP 1
    new_id=new_id.lower()
    # STEP 2
    new_id=re.sub('[^A-Za-z0-9가-힣\-_.]', '', new_id)
    # STEP 3
    while True:
        new_id=new_id.replace("..",".")
        if ".." not in new_id: break
    # STEP 4
    new_id=new_id.strip(".")
    # STEP 5
    if new_id == "":
        new_id = "a"
    # STEP 6
    if len(new_id)>15:
        new_id=new_id[:15]
    new_id=new_id.rstrip(".")
    # STEP 7
    if len(new_id)<=2:
        while True:
            new_id = new_id + new_id[-1]
            if len(new_id)>=3: break
    return new_id
