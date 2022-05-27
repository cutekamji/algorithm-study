# 월간 코드 챌린지 시즌1 - 3진법 뒤집기
# https://programmers.co.kr/learn/courses/30/lessons/68935

# int 지정시 숫자를 옵션으로 추가하면 그 수에 해당하는 n진법 변환이 가능함
def solution(n):
    s=''
    while n>0:
        n,m = divmod(n,3)
        s+=str(m)
    answer=int(s,3)
    return answer
