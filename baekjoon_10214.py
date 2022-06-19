# Coder's High 2014 - Baseball
# https://www.acmicpc.net/problem/10214

# 테스트 수 입력
n = int(input())
# 입력받은 테스트 수 만큼 반복
for i in range(n):
    # 입력받을 점수 합산용 int변수 생성 
    y_scr = 0
    k_scr = 0
    # 경기별 점수 합산
    for j in range(0,9):
        y, k = map(int,input().split())
        y_scr += y
        k_scr += k
    # 연세대 점수가 높으면 "Yonsei" 고려대가 높으면 "Korea" 비기면 "Draw" 
    if y_scr > k_scr:
        print("Yonsei")
    elif y_scr < k_scr:
        print("Korea")
    else:
        print("Draw")
