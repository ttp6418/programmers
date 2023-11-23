def solution(n):
    value = 0
    while(n != 1):
        if n % 2 == 1:
            value += 1
            n -= 1
        else: 
            n = int(n / 2)
            
    return value + 1