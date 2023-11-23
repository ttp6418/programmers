from heapq import *

def solution(numbers):
    n = len(numbers)
    answer = [-1] * n
    
    h = []
    for num in range(n):
        temp = numbers[num]
        
        while h and h[0][0] < temp:
            _, idx = heappop(h)
            answer[idx] = temp
        heappush(h, [temp, num])
    return answer