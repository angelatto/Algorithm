# 추석 트래픽 - 초당 최대 처리량이 되는 구간 윈도우를 찾는 문제
# 난이도 - 상

# 9/15 하루 동안 로그 데이터 분석 -> 날짜 버려도 됨 oh no -> 날짜 필요함. 주는데는 이유가 있음
import datetime
def solution(lines):
    # --------------전처리--------------
    logs = [] # 시작 시간과 종료 시간을 기록함
    for line in lines:
        log = line.split(' ')

        # string -> datetime -> timestamp
        timestamp = datetime.datetime.strptime(log[0] + ' ' + log[1], '%Y-%m-%d %H:%M:%S.%f').timestamp()

        logs.append((timestamp, -1)) # 종료시간 에폭시간으로 저장, flag = -1
        logs.append((timestamp - float(log[2][:-1]) + 0.001, 1)) # 시작시간 에폭시간으로 저장, flag = 1

    logs.sort(key=lambda x:x[0]) # 타임스탬프 기준으로 정렬
    print('logs: ', logs)

    # ------------최대 처리량이 되는 구간 찾기--------------
    max_request = 1




    return max_request

# print(solution(["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]))
print(solution(["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]))
