def solution(a, b):
    day_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_answer = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    
    days = 0
    
    for aa in range(1, a):
        days = days + day_month[aa-1]
    days = days + b - 1
    return day_answer[days % 7]