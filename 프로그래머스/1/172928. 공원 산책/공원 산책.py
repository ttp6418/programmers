def solution(park, routes):
    
    for i in range(len(park[0])):
        for j in range(len(park)):
            if park[j][i] == 'S':
                s_w, s_h = j, i
                break
    
    for [route_index, route] in enumerate(routes):
        head, move = route.split(" ")
        move = int(move)
        donot_flag = False
        if head == 'E' and s_h + move < len(park[0]):
            for m in range(move):
                if park[s_w][s_h + m + 1] == 'X':
                    donot_flag = True
                    break
            if donot_flag == False:
                s_h = s_h + move
        if head == 'W' and s_h - move >= 0:
            for m in range(move):
                if park[s_w][s_h - (m + 1)] == 'X':
                    donot_flag = True
                    break
            if donot_flag == False:
                s_h = s_h - move
        if head == 'S' and s_w + move < len(park):
            for m in range(move):
                if park[s_w + m + 1][s_h] == 'X':
                    donot_flag = True
                    break
            if donot_flag == False:
                s_w = s_w + move
        if head == 'N' and s_w - move >= 0:
            for m in range(move):
                if park[s_w - (m + 1)][s_h] == 'X':
                    donot_flag = True
                    break
            if donot_flag == False:
                s_w = s_w - move
        print(s_w, s_h)
    return [s_w, s_h]