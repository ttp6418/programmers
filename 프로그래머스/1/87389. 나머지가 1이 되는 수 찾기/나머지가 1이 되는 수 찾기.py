def solution(n):
    s = 2
    while(1):
        if n % s == 1:
            return s
        else: s = s + 1