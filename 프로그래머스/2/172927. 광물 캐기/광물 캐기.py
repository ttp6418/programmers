def solution(picks, minerals):
    import numpy as np
    attr = ['diamond', 'iron', 'stone']
    answer = 0
    method_per_work = 5
    new_minerals = []
    
    method_total = sum(picks)
    
    weights = []
    for m in range(int(len(minerals) / method_per_work)):
        weights_sum = 0
        for w in range(method_per_work):
            for [index_find, fin] in enumerate(attr):
                if fin == minerals[m * method_per_work + w]:
                    weights_sum = weights_sum + (5 ** (2 - index_find))
        weights.append(weights_sum)
    weights_sum = 0
    if len(minerals) % method_per_work != 0:
        for m in minerals[int(len(minerals) / method_per_work) * method_per_work:]:
            for [index_find, fin] in enumerate(attr):
                        if fin == m:
                            weights_sum = weights_sum + (5 ** (2 - index_find))
        weights.append(weights_sum)
    
    for i in range(len(weights)):
        weights_index = np.argmax(weights)
        weights[weights_index] = -1
        print(weights_index, method_total)
        if weights_index >= method_total:
            continue
        try:
            minerals_curr = minerals[weights_index * method_per_work:(weights_index + 1) * method_per_work]
        except:
            minerals_curr = minerals[weights_index * method_per_work:-1]
        
        for [method_index, method_many] in enumerate(picks):
            if method_many != 0:
                picks[method_index] = picks[method_index] - 1
                if method_index == 0:
                    answer = answer + len(minerals_curr)
                    break
                elif method_index == 1:
                    for p in minerals_curr:
                        if p != 'diamond': answer = answer + 1
                        else: answer = answer + 5
                    break
                else:
                    for p in minerals_curr:
                        if p == 'diamond': answer = answer + 25
                        elif p == 'iron': answer = answer + 5
                        else: answer = answer + 1
                    break
        
    """print(weights)
    
    for [w_index, w_value] in enumerate(weights):
        for [method_type, method_many] in enumerate(picks):
            if method_many != 0:
                if method_type == 0:
                    #del weights[0]
                    answer = answer + 5
                    picks[method_type] = picks[method_type] - 1
                    print(answer)
                    break
                elif method_type == 1:
                    #del weights[0]
                    answer = answer + int(w_value / 5)
                    picks[method_type] = picks[method_type] - 1
                    print(answer)
                    break
                else: 
                    #del weights[0]
                    answer = answer + int(w_value)
                    picks[method_type] = picks[method_type] - 1
                    print(answer)
                    break"""
                
    
    """exit_flag = False
    for [mine_index, mine] in enumerate(minerals):
        if picks[0] != 0:
            answer = answer + 1
        elif picks[1] != 0:
            if mine == 'diamond':
                answer = answer + 5
            else: answer = answer + 1
        elif picks[2] != 0:
            if mine == 'diamond':
                answer = answer + 25
            elif mine == 'iron':
                answer = answer + 5
            else: answer = answer + 1
        else:
            exit_flag = True
            break
        if exit_flag == True: break
        if mine_index % 5 == 4:
            for [p_index, p] in enumerate(picks):
                if p != 0:
                    picks[p_index] = picks[p_index] - 1
                    break"""
    return answer