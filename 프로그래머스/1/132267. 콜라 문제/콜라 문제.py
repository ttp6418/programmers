def solution(a, b, n):
    answer = 0
    
    while(int(n / a) >= 1):
        add = int(n / a) * b
        n = n % a + add
        answer = answer + add
    
    return answer