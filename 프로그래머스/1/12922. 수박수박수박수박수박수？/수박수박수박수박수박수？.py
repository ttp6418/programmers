def solution(n):
    lis = ['수', '박']
    
    answer = []
    
    for s in range(n):
        answer.append(lis[int(s % 2)])
    return "".join(answer)