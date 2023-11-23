def solution(s, skip, index):
    for [index_to, alpha] in enumerate(s):
        for m in range(index):
            s = list(s)
            while(1):
                if (ord(s[index_to]) + 1) == 123:
                    s[index_to] = 'a'
                else:
                    s[index_to] = chr(ord(s[index_to]) + 1)
                if s[index_to] not in skip:
                    break
            s = ''.join(s)
    return s