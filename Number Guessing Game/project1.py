import time
import random
import logo

def start_game():

    print(logo.logo)
    print('\n \n')
    print("Welcome to the number guessing game!")
    time.sleep(2)

    level = input("Choose a level = Easy|Hard : ").lower()

    global count
    global number
    
    number = random.randint(1,50)
    if level == 'easy':
        count = 10
    else:
        count = 5

    print(F"You chose {level} level. \n")
    print("You are going to find a number between 1-50")


def check_answer(choose):
    if count == 0:
        print(f"You Lost!! The number is {number}")
    elif (count > 0) and ((choose < number) and (number-choose in range(10))):
        print("Wow very hot but consider to go up!")
    elif (count > 0) and  (choose > number) and (choose-number in range(10)):
        print("Wow very hot but consider to go down!")
    else:
        print("UH Too Cold! You are quite far from your number.")


start_game()


while count > 0:
    print(f"You have {count} attempss")
    try:
        choose = int(input("Take a guess : "))
        if choose == number:
            print("WOW You guessed right")
            break
        elif (choose < number) and (number-choose in range(10)):
            count -= 1
            check_answer(choose)
        elif (choose > number) and (choose-number in range(10)):
            count -= 1
            check_answer(choose)
        else:
            count -= 1
            check_answer(choose)
    except ValueError as e:
        print(e)
        count -= 1







        







