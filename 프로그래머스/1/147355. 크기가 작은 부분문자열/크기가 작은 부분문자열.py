def solution(t, p):
    count = 0
    l = len(p)
    if l > 1:
        for [index, s] in enumerate(t[:-(l - 1)]):
            if int(t[index:index+l]) <= int(p): count = count + 1
    else: 
        for s in (t):
            if int(s) <= int(p): count = count + 1
        
    return count