#패킹과 언패킹
# t = [1,2,3]
# a,b,c = t
# print(a,b,c,t)

# 값과 메모리 주소값의 차이
# a = 1000000
# b = 1000000
# print(a is b)
# print(a == b)

#조건문
# print("나이를 입력하세요: ")
# myage = int(input())
# if myage > 30:
#     print("too old")
# elif myage < 10:
#     print("too young")
# else :
#     print("pass")

#반복문
# for i in [1,2,3,4,5]:
#     print(i , "hello")
#
# for i in range(10):
#     print(i)
#
# for i in "abcdefg":
#     print(i)
#
# for i in range(1, 10, 2):
#     print(i)

s = "i love you"
r = ''
for i in s:
    r = i + r
print(r)
