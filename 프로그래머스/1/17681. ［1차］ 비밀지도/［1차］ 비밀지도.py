import numpy as np

def solution(n, arr1, arr2):
    n = int(n)
    answer = np.zeros([n, n], dtype=int)
    for i in range(n):
        code1 = str(bin(arr1[i]))[2:].zfill(n)
        code2 = str(bin(arr2[i]))[2:].zfill(n)
        for j in range(n):
            answer[i][j] = answer[i][j] + int(code1[j]) + int(code2[j])
    
    result = []
    
    for k in range(n):
        temp = ''
        for s in range(n):
            if answer[k][s] >= 1:
                temp = temp + '#'
            else: temp = temp + ' '
        result.append(temp)
    return result