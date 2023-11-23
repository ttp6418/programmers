def solution(seoul):
    for [index, s] in enumerate(seoul):
        if s == 'Kim':
            return "김서방은 " + str(index) + "에 있다"