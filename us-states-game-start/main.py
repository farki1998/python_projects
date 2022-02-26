import turtle
import pandas
screen = turtle.Screen()
screen.title("US state game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
number_of_guess = []
while len(number_of_guess)<50:
    answer = screen.textinput(title=f"{len(number_of_guess)}/50 STATES CORRECT",prompt="Take a guess").title()
    data = pandas.read_csv("50_states.csv")
    z = data["state"].to_list()
    if answer in z:
        number_of_guess.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        row = data[data["state"] == answer]
        t.goto(int(row.x),int(row.y))
        t.write(answer)
screen.exitonclick()
