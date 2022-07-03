# 2019 카카오 개발자 겨울 인턴십 - 크레인 인형뽑기 게임
# https://programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    # 바구니
    bucket=[]
    # 인형이 터지지 않는다는 가정 하에 바구니에 쌓일 인형 구하기
    for line in moves:
        for i in range(len(board)):
            if board[i][line-1]==0:
                pass
            else:
                bucket.append(board[i][line-1])
                board[i][line-1] = 0
                break
    # 연속으로 동일한 인형을 담을 경우 터지는 상황 반영
    # 인형이 터질 때 카운트를 위한 변수
    cnt=0
    # 최소 반복을 바구니에 담긴 인형 수만큼 진행할 것
    for j in range(len(bucket)):
        # 직전 인형과 이번에 담긴 인형이 같을 경우
        # 카운트에 수를 더하고 bucket 리스트에서 원소 삭제
        for i in range(len(bucket)-1):
            if bucket[i]==bucket[i+1]:
                del bucket[i]
                del bucket[i]
                cnt+=2
                break
            else:
                pass
    return cnt
