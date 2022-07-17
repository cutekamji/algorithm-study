# Summer/Winter Coding(2019) - 멀쩡한 사각형
# https://school.programmers.co.kr/learn/courses/30/lessons/62048

# 내 풀이 - 일부 테스트 케이스 오답, 런타임 발생
def solution(w,h):
    # 대각선 기울기 계산
    grad = h/w
    # 멀쩡한 사각형의 개수
    cnt=0
    # 가로길이를 1씩 옮겨가면서 멀쩡한 사각형 개수 누적
    for i in range(w):
        cnt+=(grad*i)//1
    # 대칭
    answer = cnt*2
    return answer
  
# 다른 사람의 풀이
import math
def solution(w,h):
    return w*h - (w+h-math.gcd(w,h))
