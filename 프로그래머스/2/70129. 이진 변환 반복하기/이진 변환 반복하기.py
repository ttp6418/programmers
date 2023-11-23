def solution(s):
    count_do = 0
    count_zero = 0
    while(s != '1'):
        count_do = count_do + 1
        count_zero = count_zero + s.count("0")
        s = s.replace("0", "")
        num = len(s)
        s = str(bin(num))[2:]
    return [count_do, count_zero]