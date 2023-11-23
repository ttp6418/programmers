def solution(dartResult):
    answer = []
    
    #dartResult = dartResult.replace("#", "##")
    #dartResult = dartResult.replace("*", "**")
    
    aws = ['None', 'S', 'D', 'T']
    n = 0

    # 스타상(*)은 첫 번째 기회에서도 나올 수 있다. 이 경우 첫 번째 스타상(*)의 점수만 2배가 된다. (예제 4번 참고)
    while n < len(dartResult):
        if str.isdigit(dartResult[n]) != True:
            if dartResult[n] == '*':
                answer[-1] = answer[-1] * 2
                try: answer[-2] = answer[-2] * 2
                except: pass
            elif dartResult[n] == '#': answer[-1] = answer[-1] * -1
            else: pass
        else:
            if (dartResult[n] == '1' and dartResult[n+1] == '0'):
                answer.append(10 ** aws.index(dartResult[n + 2]))
                n += 2
            else:
                answer.append(int(dartResult[n]) ** aws.index(dartResult[n + 1]))
                n += 1
        n += 1
    return sum(answer[:3])