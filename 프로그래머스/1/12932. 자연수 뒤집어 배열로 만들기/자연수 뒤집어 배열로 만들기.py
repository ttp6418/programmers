def solution(n):
    n = str(n)
    n = list(n)
    n.reverse()
    #n.sort(reverse=True)
    return list(map(int, n))