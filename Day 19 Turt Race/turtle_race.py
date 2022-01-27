
from turtle import Turtle,Screen
import random

screen = Screen()
screen.setup(width=700,height=700)

turtles = {'red':'red','blue':'blue','purple':'purple','pink':'pink'}


for key,value in turtles.items():
    turt = Turtle(shape='turtle')
    turt.color(value)
    turtles.update({key:turt})

def create_screen():
    distance = 0
    for i in turtles.values():
        i.penup()
        i.setheading(225)
        i.forward(450)
        i.setheading(90)
        i.forward(100+distance)
        i.setheading(0)
        distance += 100


def movement():
    while True:
        random_movement = random.randrange(1,10)
        for key,value in turtles.items():
            random.choice(list(turtles.values())).forward(random_movement)
            if value.position()[0] > 340 :
                if user_bet == str(key):
                    print(f"You Won The winner is {user_bet} turtle")
                else:
                    print(f"You lost The winner is {key} turtle")
                return False
                

create_screen()
user_bet = screen.textinput(title='Make your bets',prompt='Which turtle will win the race? Enter a color(red,blue,purple,pink) : ').lower()
while movement():
    movement()


screen.exitonclick()

