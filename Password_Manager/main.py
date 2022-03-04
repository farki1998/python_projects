import random
from tkinter import *
from tkinter import messagebox

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    nr_letters= random.randint(8,10)
    nr_symbols = random.randint(2,4)
    nr_numbers = random.randint(2,4)
    password_ran = []
    for char in range(nr_letters):
      password_ran.append(random.choice(letters))
    for char in range(nr_symbols):
      password_ran.append(random.choice(symbols))
    for char in range(nr_numbers):
      password_ran.append(random.choice(numbers))
    x = "".join(password_ran)
    password_entry.insert(0,x)
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if len(website)==0 or len(password)==0:
        messagebox.askokcancel(title="Error",message="Dont let any fields empty")
    else:
        ok = messagebox.askokcancel(title=website,message="Are you sure?")
        if ok:
            with open("data.txt","a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0,END)
                password_entry.delete(0,END)
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)
canvas = Canvas(width=200,height=200)
image1 = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=image1)
canvas.grid(column=1,row=0)
website_label = Label(text="Website:")
website_label.grid(column=0,row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0,row=2)
password_label = Label(text="Password:")
password_label.grid(column=0,row=3)
website_entry = Entry(width=36)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()
email_entry = Entry(width=36)
email_entry.grid(row=2,column=1,columnspan=2)
password_entry = Entry(width=21)
password_entry.grid(row=3,column=1)
gen_pass = Button(text="Generate password",command=generate_password)
gen_pass.grid(row=3,column=2)
add = Button(text="Add",width=36,command=save)
add.grid(row=4,column=1,columnspan=2)
window.mainloop()
