def solution(absolutes, signs):
    sum = 0
    for [index, abso] in enumerate(absolutes):
        if signs[index] == False:
            sum = sum + abso * -1
        else: sum = sum + abso
    return sum