import turtle
from random import *
# t.pencolor(r, g, b)
# t.fillcolor(r, g, b)


t = turtle.Turtle()
t.shape('turtle')


def draw_flower(n):
    for _ in range(n):
        t.left(360 / n)
        r = random()
        t.begin_fill()
        t.pencolor(r, r, r)
        t.fillcolor(r, r, r)
        t.circle(120, 60)
        t.left(120)
        t.circle(120, 60)
        t.left(120)
        t.end_fill()
        

print('꽃잎의 개수를 입력하세요: ')
flower = int(input())


draw_flower(flower) # 6개 그리기
turtle.mainloop()