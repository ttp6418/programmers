def solution(s):
    s = s.lower()
    check = ['p', 'y']
    
    if s.count(check[0]) == s.count(check[1]): return True
    else: return False