class ClassA:
    def func1():
        print('func1')

    def func2(self):
        print(id(self)) # 4399575584
        print('func2')


f = ClassA()
f.func2()  # 명시적으로 self 객체로 넘어감
# f.func1()  # 에러 -> 아래의 클래스 이름자체로 호출하면서 해결하기
ClassA.func1()
# ClassA.func2() # 에러 - self 로 인스턴스를 넘겨받아야 하는데, 클래스 이름으로 호출하면 인스턴스를 모름
ClassA.func2(f) # 위의 에러를 이렇게 해결 -> 인스턴스를 넘겨줌

print(id(f)) # 4399575584 위에 self로 넘어간 객체와 같은 객체이다.


