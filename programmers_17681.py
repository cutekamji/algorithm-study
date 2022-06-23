# 2018 KAKAO BLIND RECRUITMENT - [1차] 비밀지도
# https://programmers.co.kr/learn/courses/30/lessons/17681

def solution(n, arr1, arr2):
    answer=[]
    # 입력받은 리스트 원소를 이진화하는 함수
    def array2bin(n,arr):
        for i in range(n):
            arr[i]=bin(arr[i])[2:].zfill(n)
        return arr
    arr1 = array2bin(n,arr1)
    arr2 = array2bin(n,arr2)
    # for i in range(n):
    #     arr1[i] = bin(arr1[i])[2:].zfill(n)
    #     arr2[i] = bin(arr2[i])[2:].zfill(n)
    
    # arr1과 arr2의 원소의 동일한 위치 값이 하나라도 1이면 #, 둘 다 0이면 공백인 원소 생성
    # 생성된 원소는 answer 리스트에 append 됨
    for i in range(n):
        word=''
        for j in range(n):
            if (arr1[i][j]=='0') & (arr2[i][j]=='0'):
                word+=' '
            else:
                word+='#'
        answer.append(word)
    return answer
