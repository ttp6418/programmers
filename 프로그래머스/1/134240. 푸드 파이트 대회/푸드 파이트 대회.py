def solution(food):
    answer = ''
    answer = list(answer)
    
    for [f_index, f] in enumerate(food[1:]):
        if f / 2 >= 1:
            for step in range(int(f/2)):
                answer.append((f_index + 1))
    rev = answer.copy()
    rev.reverse()
    answer = "".join(map(str, answer))
    answer = answer + '0' + "".join(map(str, rev))
    
    return answer