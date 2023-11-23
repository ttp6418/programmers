def solution(s):
    new_ss = []
    ss = s.split('\n')[-1].split(" ")
    for [ss_index,sss] in enumerate(ss):
        temp = ''
        try: temp = temp + str(sss[0].upper())
        except: pass
        for ssss in range(1, len(sss)):
            try: temp = temp + sss[ssss].lower()
            except:pass
        new_ss.append(temp)
    answer = ' '.join(new_ss)
    return answer