from itertools import combinations

def solution(number):
    answer = 0
    
    guess = list(combinations(number, 3))
    
    for g in guess:
        if g[0] + g[1] + g[2] == 0:
            answer = answer + 1
    
    return answer