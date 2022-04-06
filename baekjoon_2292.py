# 벌집
# https://www.acmicpc.net/source/41600750

# n : 입력받은 정수 (벌집 방 번호)
# x : 중앙에서 목적지까지 이동해야하는 최소한의 방의 수

# 접근 > x가 늘어나는 최초의 방 번호를 나열해보니 일정한 규칙으로 증가한다는 점에 초점을 둠

n = int(input())

x = 0
strt_p=0
while n>=strt_p:
    x+=1
    strt_p = 6*x*(x-1)/2+2
print(x)
