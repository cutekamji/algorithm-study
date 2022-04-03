# 줄마다 *의 개수가 하나씩 증가(좌측정렬)
num = 5
for i in range(num):
    for j in range(i+1):
        print("*", end = "")
    print("")
    

# 줄마다 *의 개수가 하나씩 감소(좌측정렬)
num = 5
for i in range(num):
    for j in range(num-i):
        print("*", end = "")
    print("")
    
 
# 줄마다 *의 개수가 하나씩 증가(우측정렬)
num = 5
for i in range(num):
    for j in range(num-1-i):
        print(" ", end = "")
    for j in range(i+1):
        print("*", end = "")
    print("")
    
    
# 줄마다 *의 개수가 하나씩 감소(우측정렬)
num = 5
for i in range(num):
    for j in range(i):
        print(" ", end = "")
    for j in range(num-i):
        print("*", end = "")
    print("")
    

# 줄마다 *의 개수가 양쪽에서 하나씩 증가(중앙정렬)
num = 5
for i in range(num):
    for j in range(num-i-1):
        print(" ", end = "")
    for j in range(2*i+1):
        print("*", end = "")
    print("")
    
    
# 줄마다 *의 개수가 양쪽에서 하나씩 감소(중앙정렬)
num = 5
for i in range(num):
    for j in range(i):
        print(" ", end = "")
    for j in range(2*(num-i)-1):
        print("*", end = "")
    print("")
    
# 줄마다 *의 개수가 양쪽에서 하나씩 감소했다가 다시증가(중앙정렬)
num = 5
for i in range(2*num+1):
    if i<=num:
        for j in range(num-i):
            print(" ", end = "")
        for j in range(2*i+1):
            print("*", end = "")
    elif i > num:
        for j in range(i-num):
            print(" ", end = "")
        for j in range(2*num-2*(i-num)+1):
            print("*", end = "")
    print("")
