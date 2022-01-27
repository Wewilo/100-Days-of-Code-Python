
from turtle import Turtle,Screen

turt = Turtle('turtle')
screen = Screen()


def forward():
    turt.forward(20)

def backward():
    turt.backward(20)

def turn_right():
    turt_heading = turt.heading() - 10
    turt.setheading(turt_heading)

def turn_left():
    turt_heading = turt.heading() + 10
    turt.setheading(turt_heading)

def make_circle():
    turt.circle(20)

def clear():
    turt.clear()
    turt.penup()
    turt.home()
    turt.pendown()


screen.onkey(forward,'w')
screen.onkey(backward,'s')
screen.onkey(turn_left,'a')
screen.onkey(turn_right,'d')
screen.onkey(make_circle,'f')
screen.onkey(clear,'c')

screen.listen()
screen.exitonclick()
