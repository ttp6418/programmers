def solution(s):
    answer = []
    index = 0
    dict = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    s_2 = s
    while(1):
        print(s_2, answer)
        try:
            temp = int(s_2[0])
            answer.append(str(temp))
            # answer[index] = str(temp)
            s_2 = s_2[1:]
        except:
            temp = str(s_2[0])
            temp_2 = str(s_2[1])
            for [ine, i] in enumerate(dict):
                if temp == str(i[0]) and temp_2 == str(i[1]):
                    answer.append(str(ine))
                    # answer[index] = str(ine)
                    s_2 = s_2[len(dict[ine]):]
                    break
        index += 1
        if len(s_2) == 0:
            break
    new_answer = 0
    for [ine, i] in enumerate(answer):
        new_answer = new_answer + int(i) * 10 ** (len(answer) - (ine + 1))
    return new_answer