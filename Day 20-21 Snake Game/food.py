from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        
        self.shape('circle')
        self.color('red')
        self.random_location()
    
    def random_location(self):
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.penup()
        self.goto(random.randint(-280,280),random.randint(-280,280))


