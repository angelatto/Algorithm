# 셔틀버스 - 쉬워 보이는데 어려운 문제, 정확하게 시간 계산, 빈틈없이 계산, 실수 요소 많음
# 난이도 - 중
# 주의 - timetable 정렬되지 않음

def solution(n, t, m, timetable):

    # 1. timetable 정렬 하기, 시간을 초 단위로 변경함
    timetable = [ int(time[:2]) * 60 + int(time[3:]) for time in timetable]
    timetable.sort()

    # 2. 버스 태우기
    current = 540  # 9시
    for _ in range(n):
        for _ in range(m): # m 명 탈 수 있음
            if timetable and timetable[0] <= current:
                 # timetable에 사람이 있다 = 대기가 있다 = 탑승가능한 마지막 사람보다 1초먼저도착
                candidate = timetable.pop(0) - 1
            else: # timetable이 empty = 대기가 없으면 가장 마지막에 도착
                candidate = current
        current += t

    # 3. candidate를 분초로 다시 변경
    h, m = divmod(candidate, 60)
    return str(h).zfill(2) + ':' + str(m).zfill(2)


print(solution(1, 1, 5, ['08:00', '08:01', '08:02', '08:03']))
print(solution(2, 10, 2, ['09:10', '09:09', '08:00']))
