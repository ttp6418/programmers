def solution(numbers):
    result = []
    for [index_curr, curr] in enumerate(numbers):
        for [index_plus, plus] in enumerate(numbers):
            if index_curr != index_plus:
                temp = curr + plus
                if temp not in result:
                    result.append(temp)
    result.sort()
    return result