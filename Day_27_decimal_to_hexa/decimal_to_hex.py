from tkinter import *

main = Tk()
main.title('Decimal To Hex Number')
main.config(padx=20,pady=20)


def convert(num):
    result = hex(int(num))
    res = Entry(main,width=20)
    res.grid(row=1,column=1)
    res.insert(0,result)
    

decimal_label = Label(main,text='Decimal : ',font=('Arial',12))
decimal_entry = Entry(main)
decimal_label.grid(row=0,column=0)
decimal_entry.grid(row=0,column=1)
hexa_entry = Label(main,text='Is equal to',font=('Arial',12),pady=10)
hexa_entry.grid(row=1,column=0)
hexa_entry2 = Label(main,text='hex number',font=('Arial',12),pady=10)
hexa_entry2.grid(row=1,column=2)
result = Button(main,text='Calculate' ,command=lambda:convert(decimal_entry.get()),padx=10,pady=5)
result.grid(row=2,column=0)


main.mainloop()