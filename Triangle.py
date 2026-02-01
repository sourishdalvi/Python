import turtle

t = turtle.Turtle()
t.speed(3)
side = 100
t.forward(side)
t.left(90)
t.forward(side)
t.left(135)
t.forward(side * 1.414)
t.penup()
t.goto(0, 0)
t.setheading(180)
t.pendown()
t.forward(side)
t.right(90)
t.forward(side)
t.right(135)
t.forward(side * 1.414)
turtle.done()


