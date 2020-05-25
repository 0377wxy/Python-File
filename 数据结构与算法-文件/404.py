import turtle


def tree(brance_len):
    if brance_len > 5:
        t.forward(brance_len)
        t.right(20)
        tree(brance_len - 15)
        t.left(40)
        tree(brance_len - 15)
        t.right(20)
        t.backward(brance_len)


t = turtle.Turtle()
t.left(90)
t.penup()
t.backward(100)
t.pendown()
t.pencolor('green')
t.pensize(2)
tree(100)
t.hideturtle()
turtle.done()
