def solution(k, score):
    honor = []
    for day in range(len(score)):
        check_temp = score[:day+1]
        check_temp.sort(reverse=True)
        if day < k:
            honor.append(check_temp[-1])
        else: honor.append(check_temp[k-1])
    return honor