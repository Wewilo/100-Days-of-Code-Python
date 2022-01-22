import random
import sys
import os
import hangman_art as art


def start_game():
    words = ['sanctuary','word','dark','souls','abstract','linux','keyboard','shadow','die','twice','learn','speak','teach']
    word = random.choice(words)
    answer = ['_'] * len(word)
    new_word = [i for i in word]
    check_answer(new_word,word,answer)


def check_answer(new_word,word,answer,life=6,count=-1):
    print(art.logo)
    while life > 0:
        print(' '.join(answer))
        print(art.stages[count])
        guess = input("Guess a letter : ").lower()
        os.system("cls")
        if guess in word:
            for index,value in enumerate(word):
                if value == guess:
                    answer[index] = guess
                    if new_word == answer:
                        print(f"{art.winner} \n \nThe word is {word}")
                        sys.exit()
        else:
            print(f"You guessed {guess}, that's not in the word. You lose a life")
            count -= 1
            life -= 1
    else:
        print(f"{art.loser} \n \nThe word is {word}")


start_game()