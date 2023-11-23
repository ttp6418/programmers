def solution(arr):
    temp = arr[0]
    answer = []
    answer.append(temp)
    for i in arr:
        if temp == i:
            pass
        else:
            answer.append(i) 
            temp = i
    return answer