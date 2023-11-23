def solution(a, b):
    answer = 0
    
    if b < a:
        temp = a
        a = b
        b = temp
    
    for s in range(a, b+1, 1):
        answer += s
    
    return answer