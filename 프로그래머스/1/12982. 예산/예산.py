def solution(d, budget):
    d.sort()
    for [index, i] in enumerate(d):
        if budget < i:
            return index
        else:
            budget = budget - i
    answer = len(d)
    return answer