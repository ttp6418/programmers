def solution(s):
    arr = []
    answer = []
    
    arr.append(s[0])
    answer.append(-1)
    
    for string in s[1:]:
        if string not in arr:
            answer.append(-1)
        else:
            for i in range(len(arr)):
                if arr[len(arr) - i - 1] == string:
                    answer.append(i + 1)
                    break
        arr.append(string)
    return answer