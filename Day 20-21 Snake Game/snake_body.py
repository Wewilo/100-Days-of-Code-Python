from turtle import Turtle, setheading

class Snake:

    def __init__(self):        
        self.snake_body = []
        self.create_snake()


    def create_snake(self):

        for segment in range(0,-60,-20):
            turt = Turtle(shape='square')
            turt.color('white')
            turt.penup()
            turt.goto(segment,0)
            self.snake_body.append(turt)

    def move(self):
        for segment in range(len(self.snake_body)-1,0,-1):
            new_x = self.snake_body[segment-1].xcor()
            new_y = self.snake_body[segment-1].ycor()
            self.snake_body[segment].goto(new_x,new_y)
        
        self.snake_body[0].forward(20)

    def increase_height(self):
            height = Turtle(shape='square')
            height.color('white')
            height.penup()
            height.goto(self.snake_body[-1].pos())
            self.snake_body.append(height)

    
    def go_up(self):
        
        if self.snake_body[0].heading() != 270:
            self.snake_body[0].setheading(90)

    def go_down(self):
        
        if self.snake_body[0].heading() != 90:
            self.snake_body[0].setheading(270)

    def go_right(self):

        if self.snake_body[0].heading() != 180:
            self.snake_body[0].setheading(0)

    def go_left(self):
        
        if self.snake_body[0].heading() != 0:
            self.snake_body[0].setheading(180)
