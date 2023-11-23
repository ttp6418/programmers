def solution(n, t, mm, timetable):
    answer = ''
    time_standard = 9 * 60
    
    for [i,time] in enumerate(timetable):
        h, m = map(int,time.split(':'))
        timetable[i] = h * 60 + m
    timetable.sort()
    timebus = [time_standard]
    
    for ns in range(n-1):
        timebus.append(time_standard + (ns + 1) * t)
    
    for bus in timebus[:-1]:
        for mmm in range(mm):
            if len(timetable) > 1:
                if bus >= timetable[0]:
                    del timetable[0]
                    
    # 소거는 다했으니까 이제 막차의 시간을 통해 가장 늦게가면서 탈수 있겠금 조정해줄것
    
    if timebus[-1] < timetable[0]:
        return str(int(timebus[-1] / 60)).zfill(2) + ":" + str(timebus[-1] % 60).zfill(2)
    else:
        if len(timetable) == mm:
            return str(int((timetable[-1] - 1) / 60)).zfill(2) + ":" + str((timetable[-1] - 1) % 60).zfill(2)
        elif len(timetable) <= mm:
            return str(int(timebus[-1] / 60)).zfill(2) + ":" + str(timebus[-1] % 60).zfill(2)
        else:
            return str(int((timetable[mm - 1] - 1) / 60)).zfill(2) + ":" + str((timetable[mm - 1] - 1) % 60).zfill(2)
    
    return answer

# 일단 시간은 분으로 환산을하고, 
# 셔틀 운행 횟수 n, 셔틀 운행 간격 t, 한 셔틀에 탈 수 있는 최대 크루 수 m, 크루가 대기열에 도착하는 시각을 모은 배열 timetable이 입력으로 주어진다.