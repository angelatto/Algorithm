import turtle

t = turtle.Turtle()
t.shape('turtle')

n = int(input('몇각형을 그릴까요?: '))

for _ in range(n):
    t.fd(100)
    t.left(360 / n)

turtle.mainloop()