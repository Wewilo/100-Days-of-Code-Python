import random
import art
import data
import time
import sys
import os


compare_1 = random.choice(data.data)
compare_2 = random.choice(data.data)

def info(py1,py2,true_answers = 0):
    while True:
        print(art.logo)
        print("Compare A : " , end ='')
        for i,j in py1.items():
            if i == 'follower_count':
                pass
            else:
                print(j,end='  ')

        print(art.vs)

        print("Againts B : " , end ='')
        for i,j in py2.items():
            if i == 'follower_count':
                pass
            else:
                print(j,end='  ')
        choose = input("Who has more followers? Type 'A' or 'B' : ").lower()
        return check_answer(choose,true_answers,py1,py2)



def check_answer(choose,true_answers,py1,py2):
    if choose == 'a':
        if py1["follower_count"] > py2["follower_count"]:
            true_answers += 1
            print(f"You are right! Current Score : {true_answers} \n \n")
            new_py_2 = random.choice(data.data)          
            time.sleep(2)
            os.system('cls')
            info(py1,new_py_2,true_answers)
        elif py1["follower_count"] == py2["follower_count"]:
            print(f"They are same but you lost :( \n True Answers == {true_answers}")
        else:
            print(f"You lost Game Over! Final Score is : {true_answers}")
            time.sleep(2)
            sys.exit()
    if choose == 'b':
        if py2["follower_count"] > py1["follower_count"]:
            true_answers += 1
            print(f"You are right! Current Score : {true_answers} \n \n")
            new_py1 = random.choice(data.data)
            time.sleep(2)
            os.system('cls')
            info(py2,new_py1,true_answers)
        elif py2["follower_count"] == py1["follower_count"]:
            print(f"They are same but you lost :( \n True Answers == {true_answers}")
        else:
            print(f"You lost Game Over! Final Score is : {true_answers}")
            time.sleep(2)
            sys.exit()


info(compare_1,compare_2)
