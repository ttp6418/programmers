def solution(s):
    answer = True
    
    num = [48, 49, 50, 51, 52, 53, 54, 55, 56, 57]
    
    if len(s) != 4 and len(s) != 6:
        return False
    
    for i in s:
        if ord(i) not in num:
            answer = False
            break
    
    return answer