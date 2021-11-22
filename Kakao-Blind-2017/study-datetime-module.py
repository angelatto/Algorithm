import datetime

#***********************************************************
now = datetime.datetime.now()
# print('now: ', now)
# print('%d년 %d월 %d일' % (now.year, now.month, now.day))
print('%d:%d:%d' % (now.hour, now.minute, now.second))
print('%.2d:%.2d:%.2d' % (now.hour, now.minute, now.second))

#***********************************************************
# 1. String -> datetime
date_string = '2021-01-12 13:02:05'
date = datetime.datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')

# 2. datetime -> timestamp
timestamp = date.timestamp()

# 3. timestamp -> datetime
timestamp = 1463460958000
datetimeobj = datetime.datetime.fromtimestamp(timestamp/1000)
