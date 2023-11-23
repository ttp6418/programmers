def solution(phone_book):
    answer = True
    
    phone_book.sort()
    
    for p in range(1, len(phone_book)):
        if phone_book[p-1] in phone_book[p][:len(phone_book[p-1])]:
            answer = False
            break
    return answer