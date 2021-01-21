import turtle

t = turtle.Turtle()
t.shape('turtle')


# 정사각형 그리기
def draw(n):  # 한 변의 길이가 n
    for _ in range(4):
        t.circle(n)
        t.left(90)
    return


draw(100)
turtle.exitonclick()
