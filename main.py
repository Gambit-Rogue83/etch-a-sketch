from turtle import Turtle, Screen

py = Turtle()
screen = Screen()


def forward():
    py.fd(10)


def backward():
    py.bk(10)


def left_rotate():
    new_head = py.heading() + 10
    py.seth(new_head)


def right_rotate():
    new_head = py.heading() - 10
    py.seth(new_head)


def clear():
    py.clear()
    py.penup()
    py.home()
    py.pendown()

screen.listen()
screen.onkey(key='w', fun=forward)
screen.onkey(key='s', fun=backward)
screen.onkey(key='a', fun=left_rotate)
screen.onkey(key='d', fun=right_rotate)
screen.onkey(key='c', fun=clear)
screen.exitonclick()



