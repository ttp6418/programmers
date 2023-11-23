def solution(today, terms, privacies):
    answer = []
    
    today_y, today_m, today_d = today.split('\n')[0].split('.')
    
    today_date = int(today_y) * 29 * 12 + (int(today_m) - 1) * 29 + int(today_d)
    
    for [p_index, p] in enumerate(privacies):
        ps, p_p = p.split('\n')[0].split(' ')
        p_y, p_m, p_d = ps.split('\n')[0].split('.')
        
        p_date = int(p_y) * 29 * 12 + (int(p_m) - 1) * 29 + int(p_d)
        
        for t in terms:
            t_alpha, t_month = t.split("\n")[0].split(' ')
            if t_alpha == p_p:
                month_plus = int(t_month)
                break
        if p_date + month_plus * 29 <= today_date:
            answer.append(p_index + 1)
    
    return answer