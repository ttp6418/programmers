def solution(s):
    ss = s.split('\n')[0].split(" ")
    answer = []
    
    for sss in ss:
        for [ss_index, ssss] in enumerate(sss):
            if ss_index % 2 == 0: answer.append(sss[ss_index].upper())
            else: answer.append(sss[ss_index].lower())
        answer.append(" ")
    
    return "".join(answer)[:-1]