BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import random
import pandas
data = pandas.read_csv("data/french_words.csv")
learn = data.to_dict("records")
random_word = {}



def next_step():
    global random_word
    global flip_timer
    random_word = random.choice(learn)
    x = random_word["French"]
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_fun, text=x)
    canvas.itemconfig(french_image,image=card_front)
    flip_timer = window.after(3000,func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English")
    canvas.itemconfig(card_fun,text=random_word["English"])
    canvas.itemconfig(french_image,image=card_back)


def known():
    learn.remove(random_word)
    data = pandas.DataFrame(learn)
    data.to_csv("words_to_learn.csv")
    next_step()

window = Tk()
window.title("Flash Card")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
flip_timer = window.after(3000,func=flip_card)

card_front = PhotoImage(file="data/images/card_front.png")
card_back = PhotoImage(file="data/images/card_back.png")
canvas = Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthick=0)
french_image = canvas.create_image(400,263,image=card_front)
card_title = canvas.create_text(400,150,text="",font=("Ariel",40,"italic"))
card_fun = canvas.create_text(400,263,text="",font=("Ariel",60,"bold"))
canvas.grid(column=1,row=1)
ok = PhotoImage(file="data/images/right.png")
right = Button(image=ok, highlightthickness=0, command=known)
right.grid(column=0,row=4)

no = PhotoImage(file="data/images/wrong.png")
wrong = Button(image=no, highlightthickness=0,command=next_step)
wrong.grid(column=3,row=4)

next_step()
window.mainloop()
