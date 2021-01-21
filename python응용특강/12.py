import turtle
import math

t = turtle.Turtle()
t.shape('turtle')
t.speed(0)
t.pensize(7)  # 선의 굵기 10이 최대

# 오륜기 그리기
colors = ['blue', 'black', 'red', 'green', 'yellow']


def draw(r, a, b):
    x, y = a, b  # 시작 좌표

    for i in range(5):
        if i < 3:  # 위의 원 2개
            x += math.sqrt(3) * r
            y = 0
        elif i == 3:
            x -= math.sqrt(3) * r / 2
            y = 3 * r * (-1) / 2
        else:
            x -= 2 * r
            y = 3 * r * (-1) / 2

        t.up()
        t.goto(x, y)
        t.down()
        t.pencolor(colors[i])
        t.circle(r)


# print('원의 반지름을 입력하세요: ', end='')
# n = int(input())
draw(70, -200, 0)  # 반지름과, 시작좌표 넘겨줌
turtle.mainloop()
