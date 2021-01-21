"""
- 모듈 : 표준, 사용자 정의, 서드파티
- turtle 그래픽 모듈
"""
import turtle


t = turtle.Turtle()
t.shape('turtle')
t.forward(100)
t.right(90)
t.fd(100)

t.circle(80)
t.color('pink')

t.clear()

t.color('blue')
t.goto(0,0)  # 특정 좌표로 이동

t.pencolor('green')
t.fd(100)

t.pensize(10)  # 선의 굵기 10이 최대
t.fd(100)
t.speed(0)  # 거북이가 움직이는 속도 (빠르기 0 > 10 > 9 > .... > 1)


# turtle.exitonclick()
turtle.mainloop()