# 분수찾기
# https://www.acmicpc.net/problem/1193

# cnt : N번째 분수. 정수N
# line : 몇 번째 대각선에 위치하는지 (짝/홀에 따라 방향이 따름)
# end_l : N번째 대각선 중 가장 마지막 위치

cnt = int(input())
line = 1
end_l = 1
while cnt > end_l:
    line+=1
    end_l = line*(line+1)/2
#print(f'line : {line}')
#print(f'end_l : {end_l}')
diff = end_l - cnt
if line%2==0:
    target_t = int(line-diff)
    target_b = int(1+diff)
else:
    target_t = int(1+diff)
    target_b = int(line-diff)
print(f'{target_t}/{target_b}')
        
