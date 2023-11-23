import numpy as np
def solution(k, m, score):
    value = 0
    arr = np.zeros(k+1)
    for i in range(k):
        arr[i] = score.count(k-i)
    for [index,i] in enumerate(arr[:-1]):
        i = int(i)
        while(1):
            if arr[index] < m:
                arr[index+1] = arr[index+1] + arr[index]
                break
            else: 
                value = value + m * (k - index)
                arr[index] = arr[index] - m
    return value