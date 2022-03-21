import requests
from tkinter import *
def get_quote():
    response = requests.get("https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()
    quote = data["quote"]
    canvas.itemconfig(quote_text,text=quote)
YELLOW = "#f7f5dd"
window = Tk()
window.title("Kanye West quotes")
window.config(padx=50,pady=50)
canvas = Canvas(width=300,height=414)
background = PhotoImage(file="background.png")
canvas.create_image(150,207,image=background)
quote_text=canvas.create_text(150,207,text="XX",width=250,font=("Ariel",30,"bold"))
canvas.grid(row=0,column=0)
ye = PhotoImage(file="kanye.png")
ye_button = Button(image=ye,highlightthickness=0,command=get_quote)
ye_button.grid(row=1,column=0)
get_quote()
window.mainloop()
