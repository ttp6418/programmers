def solution(s):
    num = list(map(int, s.split('\n')[0].split(' ')))
    return str(min(num)) + ' ' + str(max(num))