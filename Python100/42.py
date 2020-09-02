import datetime

a = 5; b = 24 #5월 24일 -> 무슨 요일인지 반환

m = int(input())
d = int(input())

def findDay(a,b):
    day = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
    return day[datetime.date(2020,a,b).weekday()]
    #월요일이 0 일요일이 6이다. 
print(findDay(m,d))
