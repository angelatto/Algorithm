import turtle

t = turtle.Turtle()
t.shape('turtle')


def hexagon(c):
    if c == 6:
        return
    t.fd(100)
    t.right(60)
    for _ in range(6):
        t.fd(100)
        t.left(360 / 6)
    hexagon(c+1)


hexagon(0)
turtle.mainloop()