def solution(arr):
    if len(arr) <= 1:
        return [-1]
    min = arr[0]
    for i in arr:
        if min > i:
            min = i
    new_arr = arr.copy()
    new_arr.remove(min)
    return new_arr