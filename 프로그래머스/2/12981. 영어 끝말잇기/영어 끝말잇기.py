def solution(n, words):
    import math
    record_list = []
        
    for [index, word] in enumerate(words):
        if word not in record_list:
            record_list.append(word)
            if index != 0:
                if word[0] != words[index - 1][-1]:
                    print(index / n)
                    return[(index % n) + 1, math.floor(index / n) + 1]
        else: 
            return[(index % n) + 1, math.floor(index / n) + 1]
    return [0, 0]