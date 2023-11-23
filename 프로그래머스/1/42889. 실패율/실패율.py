import numpy as np

def solution(N, stages):
    answer = [0] * (N + 1)
    fail = [0] * (N)
    
    for i in stages:
        for j in range(0, i):
            answer[j] += 1
    for i in range(len(answer)-1):
        try:
            fail[i] = np.abs((answer[i+1]-answer[i]) / answer[i])
        except: fail[i] = 0
    answer = [0] * N
    for i in range(len(fail)):
        temp = np.argmax(fail)
        answer[i] = temp + 1
        fail[temp] = -99
    return np.array(answer).tolist()