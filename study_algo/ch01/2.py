"""
오늘날 가장 널리 쓰이는 IEEE754 표준에서는 실수형을 저장하기 위해
4바이트 혹은 8바이트의 고정된 크기의 메모리를 할당하므로
컴퓨터 시스템은 실수 정보를 표현하는 정확도에 한계를 가짐

개발과정에서 실수 값을 제대로 비교하지 못해서 원하는 결과를 얻지 못할 수 있음
이럴 때는 round() 함수를 이용할 수 있으며 이러한 방법이 권장됨
"""

a = 0.3 + 0.6
print(a)

if a == 0.9:
    print(True)
else:
    print(False)


a = 0.3 + 0.6
print(round(a, 1))

if round(a, 1) == 0.9:
    print(True)
else:
    print(False)