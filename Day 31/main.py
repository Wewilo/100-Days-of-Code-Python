from tkinter import *
from tkinter import PhotoImage
from turtle import width
import pandas
import random

words = {}



BACKGROUND_COLOR = "#B1DDC6"
try:
    data = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pandas.read_csv('data/french_words.csv')
    words = original_data.to_dict(orient='records')
else:
    words = data.to_dict(orient='records')

def next_word():
    cnv.itemconfig(canvas_image,image=old_image)
    global random_word 
    global flip_timer
    window.after_cancel(flip_timer)
    random_word = random.choice(words)
    cnv.itemconfig(card_title,text='French',fill='Black')
    cnv.itemconfig(card_word,text=random_word['French'],fill='Black')
    flip_timer = window.after(3000,flip_card)


def flip_card():
    cnv.itemconfig(canvas_image,image=new_image)
    cnv.itemconfig(card_title,text='English',fill='white')
    cnv.itemconfig(card_word,text=random_word['English'],fill='white')


def delete_word():
    print(len(words))
    words.remove(random_word)
    data = pandas.DataFrame(words)
    data.to_csv('data/words_to_learn.csv',index=False)
    next_word()

window = Tk()
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)


flip_timer = window.after(3000,flip_card)

cross_image = PhotoImage(file="images/right.png")
unknown_image = PhotoImage(file='images/wrong.png')

cnv = Canvas(width=800,height=526,bg=BACKGROUND_COLOR)
new_image = PhotoImage(file="images/card_back.png")
old_image = PhotoImage(file="images/card_front.png")
canvas_image = cnv.create_image(400, 263, image=old_image)
cnv.config(highlightthickness=0)
cnv.grid(row=0,column=0,columnspan=2,pady=50)


card_title = cnv.create_text(400,150,text='French',font=('Ariel','40','italic'))
card_word = cnv.create_text(400,263,text='trauve',font=('Ariel','60','bold'))

know_button = Button(image=cross_image, highlightthickness=0,bg=BACKGROUND_COLOR,relief='flat',command=delete_word)

know_button.grid(row=1,column=0)

unknow_button = Button(image=unknown_image, highlightthickness=0,bg=BACKGROUND_COLOR,relief='flat',command=next_word)
unknow_button.grid(row=1,column=1)


next_word()




window.mainloop()

