import time

#***********************************************************
print('time.time(): ', time.time())
# 현재시간
# 1970년 1월 1일 자정을 기준으로 경과한 시간을 초 단위로 표현
# Epoch 에폭 시간 또는 유닉스 시간이라고 부름
# 시간을 딱 하나의 수치값으로 1차원화하여 간단히 표현할 수 있음

#***********************************************************
t = time.time()
print('time.ctime(t): ', time.ctime(t))
# 인수로 에폭 시간을 넘기면 문자열로 바꿔준다.

#***********************************************************
print('time.localtime(t): ', time.localtime(t))
# 지역 시간을 고려하여 현지 시간을 구함

print('time.gmtime(t): ', time.gmtime(t))
# 세계 표준시인 UTC 시간을 구함

#***********************************************************
now = time.localtime()
print("%d년 %d월 %d일" % (now.tm_year, now.tm_mon, now.tm_mday))
print("%d:%d:%d" % (now.tm_hour, now.tm_min, now.tm_sec))

#***********************************************************

# 실행시간 측정
# start = time.time()
# for a in range(5):
#     print(a)
# end = time.time()
# print(end-start)

#***********************************************************
