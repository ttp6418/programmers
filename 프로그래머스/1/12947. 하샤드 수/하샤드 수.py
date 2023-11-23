def solution(x):
    x_s = str(x)
    sum = 0
    for ss in x_s:
        sum += int(ss)
    if x % sum == 0: return True
    else: return False