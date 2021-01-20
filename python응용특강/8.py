"""
- getter & setter

- 파이썬에서는 캡슐화를 제공하지 않고, 접근 제한자도 없이 은닉이 지원되지 않음
-> 비공개 속성을 위해선 변수 혹은 함수 앞에 언더바를 붙여야 한다.

- 생성자 다형성도 없다.
- 생성자 오버로딩은 지원한다.
"""


class MyCar(object):
    color = ''  # 필드 : 인스턴스 변수
    speed = 0  # 인스턴스 변수
    count = 0  # 클래스 변수

    def __init__(self, color, speed):  # 기본 생성자
        self.color = color  # self 와 같이 사용하면 인스턴스 변수
        self.speed = speed
        MyCar.count += 1  # 클래스 변수

    def upSpeed(self, value):
        self.speed += value

    def downSpeed(self, value):
        self.speed -= value


c = MyCar('빨강', 30)
print('자동차의 색상은 %s이며, 현재 속도는 %dkm이다.' % (c.color, c.speed))
c.downSpeed(20)
print('자동차의 색상은 %s이며, 현재 속도는 %dkm이다.' % (c.color, c.speed))