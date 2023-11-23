import numpy as np

def solution(x, n):
    if x != 0:
        answer = []
        for i in range(np.abs(x), np.abs(x) * n + 1, np.abs(x)):
            if x < 0: answer.append(i * -1)
            else: answer.append(i)
        return answer
    else: return [0]*n