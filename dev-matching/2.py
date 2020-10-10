def solution(p,n):
    l_12 = p.split()

    time = l_12[1].split(":")
    prehour, preminute, presecond = int(time[0]), int(time[1]), int(time[2])

    # n초 후의 시간 구하기
    hour, minute, second = prehour, preminute, presecond
    a, b = divmod(n, 60)
    if a >= 60: # 분
        h, a = divmod(a, 60)
        print(h, a)
        if h >= 24: # 시
            d, h = divmod(h, 24)
            print(d, h)
        hour += h

    minute += a
    second += b
    if minute >= 60:
        minute = 0
        hour += 1
        if prehour < 12 and hour >= 12 and l_12[0] == "AM":
            l_12[0] = "PM"
        elif prehour < 12 and hour >= 12 and l_12[0] == "PM":
            l_12[0] = "AM"
    else:
        if second >= 60:
            second = 0
            minute += 1
            if minute >= 60:
                minute = 0
                hour += 1
                if prehour < 12 and hour >= 12 and l_12[0] == "AM":
                    l_12[0] = "PM"
                elif prehour < 12 and hour >= 12 and l_12[0] == "PM":
                    l_12[0] = "AM"

    print(hour, minute, second, l_12[0])
    if l_12[0] == "AM":
        if hour == 12:
            hour = 0
    else: #pm일 때
        if 1 <= hour <= 11:
            hour += 12

    hour, minute, second = str(hour), str(minute), str(second)
    # 패딩 신경쓰기
    if len(hour) == 1:
        hour = "0"+hour
    if len(minute) == 1:
        minute = "0"+minute
    if len(second) == 1:
        second = "0"+second

    answer = hour + ":" + minute + ":" + second
    return answer

print(solution("PM 11:59:00", 200000))
