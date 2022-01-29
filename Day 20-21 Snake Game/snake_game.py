from turtle import Turtle,Screen
import time
from snake_body import Snake
from food import Food
from scoreboard import ScoreBoard


screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title('Snake')

screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.go_up,'Up')
screen.onkey(snake.go_down,'Down')
screen.onkey(snake.go_right,'Right')
screen.onkey(snake.go_left,'Left')

scoreboard = ScoreBoard()
game_is_on = True

while game_is_on:

    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.snake_body[0].distance(food) < 15:
        scoreboard.increase_score()
        snake.increase_height()
        food.random_location()
    if snake.snake_body[0].pos()[0] > 290 or snake.snake_body[0].pos()[1] > 290 or snake.snake_body[0].pos()[0] < -290 or snake.snake_body[0].pos()[1] < -290:
        scoreboard.game_over()
        game_is_on = False
    
    for segment in snake.snake_body:
        if segment == snake.snake_body[0]:
            pass
        elif snake.snake_body[0].distance(segment) < 10:

            game_is_on = False
            scoreboard.game_over()















screen.exitonclick()