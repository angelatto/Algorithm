import turtle

#  삼각형 그리기
t = turtle.Turtle()
t.shape('turtle')

for i in range(3):
    t.fd(80)
    t.right(120)

t.up()  # 선을 안그리고 이동할 때
t.left(90)
t.fd(100)

t.down() # 다시 선을 그리면서 이동할 때
t.circle(100)
t.goto(80, 90)

# 원 두 개를 연결해서 그리기
t.goto(0,0)
t.circle(50)
t.up()
t.goto(100, 0)
t.down()
t.circle(50)

t.circle(100)
t.right(180)
t.circle(100)

turtle.exitonclick()
