# 오븐 시계
# https://www.acmicpc.net/problem/2525

# 변수 설명
# h : 입력 시간(시)
# m : 입력 시간(분)
# len : 오븐 사용 시간(분)

# 제출 답안
h, m = map(int, input().split())
len = int(input())
# print(f'{h}:{m}')
# print(len)

m2 = (m+len)%60
h_add = (m+len)//60
h2 = (h+h_add)%24
# print(h_add)

print(h2, m2, end=' ')
