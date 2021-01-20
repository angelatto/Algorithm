"""
- static method : 인스턴스 생성안해도 메소드 실행 가능 (self 인자 없음)

"""


class hello:
    num = 10

    @staticmethod
    def cal(x):
        return x + 10


print(hello.cal(10))
