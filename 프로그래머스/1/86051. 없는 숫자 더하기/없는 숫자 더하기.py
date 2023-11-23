def solution(numbers):
    answer = 0
    for i in range(10):
        answer = answer + i
        for j in numbers:
            if i == j:
                answer = answer - i
    return answer