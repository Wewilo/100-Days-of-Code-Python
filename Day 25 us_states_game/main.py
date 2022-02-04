import turtle
import pandas as pd

screen = turtle.Screen()

screen.title('U.S. States Game')

screen.bgpic('game_imgg.gif')

data = pd.read_csv('50_states.csv')

turt_answer = turtle.Turtle(visible=False)

score = 0
all_states = data['state'].to_list()
total_question = len(all_states)


while score < 50:

    answer = screen.textinput(title=f'{score}/{total_question} States Correct',prompt=f"What is another state's name").title()

    state_loc = data[data['state']==answer]

    if answer == 'Exit':
        learn_states = pd.DataFrame(all_states)
        learn_states.to_csv("learn these states",index=False)
        break

    for iter in all_states:
        if iter == answer:
            score+=1
            turt_answer.penup()
            turt_answer.goto(int(state_loc.x),int(state_loc.y))
            turtle.onscreenclick(turt_answer.write(answer))
            all_states.remove(iter)

        



