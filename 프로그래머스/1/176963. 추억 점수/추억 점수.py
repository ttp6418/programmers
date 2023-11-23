def solution(name, yearning, photo):
    answer = []
    for phot in photo:
        score = 0
        for pho in phot:
            if pho in name:
                temp = name.index(pho)
                score = score + yearning[temp]
        answer.append(score)
    return answer