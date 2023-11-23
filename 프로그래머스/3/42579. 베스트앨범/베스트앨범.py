import numpy as np

def solution(genres, plays):
    answer = []
    
    genres_unique = list(set(genres))
    genres_play = [0] * len(genres_unique)
    
    for [g_index, g] in enumerate(genres):
        genres_play[genres_unique.index(g)] += plays[g_index]
    
    for gu in range(len(genres_unique)):
        temp_gu = np.argmax(genres_play)
        temp_gu2 = genres_unique[temp_gu]
        del genres_play[temp_gu]
        del genres_unique[temp_gu]
        
        grs = []
        for [gr_index, gr] in enumerate(genres):
            if gr == temp_gu2:
                grs.append([plays[gr_index], gr_index])
        grs.sort(reverse=True)
        if len(grs) >= 2:
            if grs[0][0] == grs[1][0]:
                if grs[0][1] < grs[1][1]:
                    grs_max = grs[1][1]
                    grs_min = grs[0][1]
                else:
                    grs_max = grs[0][1]
                    grs_min = grs[1][1]
                answer.append(grs_min)
                answer.append(grs_max)
            else:
                answer.append(grs[0][1])
                try: answer.append(grs[1][1])
                except: pass
        else: answer.append(grs[0][1])
    return answer