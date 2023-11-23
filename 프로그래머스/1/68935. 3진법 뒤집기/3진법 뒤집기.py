def solution(n):
    n_third = ''

    while n > 0:
        n, mod = divmod(n, 3)
        n_third += str(mod)

    return int(n_third, 3)