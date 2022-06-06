# Mystery
# https://www.acmicpc.net/problem/10212

# random 함수를 사용하도록 유도하는 문제같음
# 채점 시 운에 맞겨야 통과됨 (본인의 경우 동일 코드를 3번 제출하고 통과됨)

import random

x = random.randint(0,1)
if x > 0.5:
    print("Yonsei")
else:
    print("Korea")
