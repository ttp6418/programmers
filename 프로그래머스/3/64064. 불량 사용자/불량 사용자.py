import re
from itertools import permutations

def solution(user_id, banned_id):
    answer = []
    banned_id = [i.replace("*", ".") for i in banned_id]
    
    n = len(banned_id)
    
    for i in permutations(user_id, n):
        i = list(i)
        answer_flag = True
        for j in range(n):
            if re.match(banned_id[j], i[j]) and (len(banned_id[j]) == len(i[j])):
                continue
            else:
                answer_flag=False
                break
        if answer_flag == True:
            if sorted(i) not in answer:
                answer.append(sorted(i))
    
    return len(answer)