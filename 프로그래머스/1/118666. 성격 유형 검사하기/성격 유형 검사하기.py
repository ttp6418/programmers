def solution(survey, choices):
    answer = []
    
    score_list = [-3, -2, -1, 0, 1, 2, 3]
    personal_score = [0, 0, 0, 0]
    personal_list = ['RT', 'CF', 'JM', 'AN'] # left - right +
    
    for [index, sur] in enumerate(survey):
        for [index_personality, personality] in enumerate(personal_list):
            if sur[1] == personality[1]:
                personal_score[index_personality] = personal_score[index_personality] + score_list[choices[index]-1]
            elif sur[0] == personality[1]:
                personal_score[index_personality] = personal_score[index_personality] + score_list[choices[index]-1] * -1
    
    for [p_index, p] in enumerate(personal_score):
        if p > 0:
            answer.append(personal_list[p_index][1])
        else:
            answer.append(personal_list[p_index][0])
    return ''.join(answer)