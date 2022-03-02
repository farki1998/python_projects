from tkinter import *
import math
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Ariel"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    title.config(text="Timer")
    check.config(text="")
    global reps
    reps = 0
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN*60
    break_sec = SHORT_BREAK_MIN*60
    long_break = LONG_BREAK_MIN*60
    if reps%8==0:
        title.config(text="Long Break",fg=RED)
        count_down(long_break)
    elif reps%2==0:
        title.config(text="Work",fg=GREEN)
        count_down(work_sec)
    else:
        title.config(text="Short Break",fg=PINK)
        count_down(break_sec)
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count%60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer = window.after(1000,count_down,count-1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(reps/2)):
            mark += "✓"
        check.config(text=mark)
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)
title = Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,30,"bold"))
title.grid(column=2,row=0)
canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthick=0)
image_tomato = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=image_tomato)
timer_text=canvas.create_text(103,130,text="00:00",fill="white",font=(FONT_NAME,30,"bold"))
canvas.grid(column=2,row=2)
start_button = Button(text="Start",highlightthick=0,command=start_timer)
start_button.grid(column=1,row=3)
reset_button = Button(text="Reset",highlightthick=0,command=reset_timer)
reset_button.grid(column=3,row=3)
check = Label(fg=GREEN,bg=YELLOW,font=(FONT_NAME,30,"bold"))
check.grid(column=2,row=3)






window.mainloop()
