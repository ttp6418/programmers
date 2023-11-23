def solution(lottos, win_nums):
    joker = 0
    check = 0
    for i in lottos:
        if i == 0:
            joker = joker + 1
        for j in win_nums:
            if i == j:
                check = check + 1
    answer = []
    temp = 7 - (check + joker)
    if temp > 6:
        answer.append(6)
    else:
        answer.append(temp)
    if 7 - check == 7:
        answer.append(6)
    else:
        answer.append(7 - check)
    return answer