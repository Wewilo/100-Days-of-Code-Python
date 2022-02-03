import turtle as t
from turtle import Screen
import random

turt = t.Turtle()
turt_screen = Screen()
turt_screen.setup(width=600,height=600)
t.colormode(255)
color_list = [(250, 249, 249), (207, 165, 165), (164, 169, 169), (140, 48, 48), (244, 79, 79), (3, 144, 144), (241, 66, 66), (249, 220, 220), (2, 142, 142), (162, 55, 55)]
turt.speed(10)

distance = 0

def initial_position(distance):
    turt.hideturtle()
    turt.penup()
    turt.goto(-250,(-250+distance))
    turt.pendown()


for iter1 in range(10):
    initial_position(distance)
    distance += 50
    for iter2 in range(10):
        turt.dot(20,random.choice(color_list))
        turt.penup()
        turt.forward(50)


turt_screen.exitonclick()
