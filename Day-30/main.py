from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
import os

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for item in range(nr_letters)]
    password_symbols = [random.choice(symbols) for item in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for item in range(nr_numbers)]

    password_list = password_numbers+password_letters+password_symbols
    random.shuffle(password_list)

    password = ''.join(password_list)
    #pyperclip is allows us to copy our password to clipboard so you dont have to copy and paste.
    pyperclip.copy(password)
    password_entry.insert(0,password)
 
# ---------------------------- SAVE PASSWORD ------------------------------- #
 
def data_to_file(website,email,password):

    credentials = {
        website: {
            'email':email,
            'password':password,
        }
    }

    #If there is empty field the program will show warning and wont save your credentials else it will ask you is the information correct? if you press ok it will save to a file
    if len(website) < 1 or len(email) < 1 or len(password) <1:
        messagebox.showwarning(title='Error',message="Don't leave any empty field.")
    else:
        #is_okay will return us a booolean value so if the user pressed ok it will give us 1 else 0 and nothing will happen
        is_okay = messagebox.askokcancel(title=website,message=f'There are the details entered : \nWebsite: {str(website)}\nEmail: {str(email)}\nPassword: {str(password)}')

        if is_okay:
            messagebox.showinfo(title='Succesfull',message='Your credentials has been successfully added to the file')
            try:
                with open('my_pass.json','r') as my_passwords:
                    data = json.load(my_passwords)
            except FileNotFoundError:
                with open('my_pass.json','w') as my_passwords:
                    json.dump(credentials,my_passwords,indent=4)
            else:
                with open('my_pass.json','w') as my_passwords:
                    data.update(credentials)
                    json.dump(data,my_passwords,indent=4)

            finally:   
                website_entry.delete(0,END)
                email_entry.delete(0,END)
                password_entry.delete(0,END)
        else:
            pass



#Find Password 

def find_password():
    email = website_entry.get()
    try:
        with open('my_pass.json','r') as my_pass:
            data = json.load(my_pass)
        messagebox.showinfo(message=f"Email : {data[email]['email']}\nPassword: {data[email]['password']}")
    except KeyError:
        messagebox.showwarning('Opps',message='No Details for the website exist!')
    except FileNotFoundError:
        messagebox.showwarning(title='Opps',message='No data file found')



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
 
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)
 
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
 
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1,sticky="EW")
website_entry.focus()

search_button = Button(text='Search',width=24,command=find_password)
search_button.grid(row=1,column=2,padx=5,pady=5)



email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
 
email_entry = Entry(width=35)
email_entry.insert(0,'@gmail.com')
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
 
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
 
password_entry = Entry(width=24)
password_entry.grid(column=1, row=3, sticky="W")
 
password_button= Button(text="Generate Password",command=generate_password)
password_button.grid(column=2, row=3, sticky="EW",padx=5,pady=5)
 
add_button= Button(text="Add", width=36,command=lambda:data_to_file(website_entry.get(),email_entry.get(),password_entry.get()))
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")






window.mainloop()