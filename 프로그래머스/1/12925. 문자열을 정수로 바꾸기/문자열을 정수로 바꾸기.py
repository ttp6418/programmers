def solution(s):
    if s[0].isdigit:
        num = int(s)
        info = ''
    else:
        info = s[0]
        num = int(s[1:])
    
    if info == '-': return (-1 * num)
    else: return num