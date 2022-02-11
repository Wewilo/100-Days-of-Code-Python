from tkinter import *
import math
from playsound import playsound

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
repeat = 0
timer = 0

main = Tk()
main.title('Pomodoro')
main.config(padx=100,pady=50,bg=YELLOW)

def start_but():
    global repeat
    repeat += 1
    work = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN*60
    if repeat % 2 != 0:
        count_down(work)
        timer_label.config(fg = GREEN,text='Work')
    elif repeat % 8 == 0:
        count_down(long_break)
        timer_label.config(fg=RED,text='Break')
    else:
        timer_label.config(fg = PINK,text='Break')
        count_down(short_break)


def reset_button():
    global repeat
    main.after_cancel(timer)
    canvas.itemconfig(timer_text,text='00:00')
    timer_label.config(text='Timer')
    repeat = 0

def count_down(count):
    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'

    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = main.after(1000, count_down, count - 1)
    else:
        playsound('yamete.mp3')
        start_but()
        if repeat % 2==0 and repeat > 0:
            check_mark = Label(bg=YELLOW,fg=GREEN)
            check_mark.config(text='✔️')
            check_mark.grid(row=3,column=1)




canvas = Canvas(width=200,height=223,bg=YELLOW,highlightthickness=0)

tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(100,130,text='00:00',fill='white',font=(FONT_NAME,35,'bold'))

canvas.grid(row=1,column=1)
timer_label = Label(main,text='Timer',fg=GREEN,bg=YELLOW,font=(FONT_NAME,35))
timer_label.grid(row=0,column=1)

start_button = Button(main,text='Start',bg='white',highlightthickness=0,command=start_but)
start_button.grid(row=2,column=0)


res_button = Button(main,text='Reset',bg='white',highlightthickness=0,command = reset_button)
res_button.grid(row=2,column=2)



main.mainloop()