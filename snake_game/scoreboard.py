from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.write(f"Score: {self.score}",move=False,align="center",font=("Ariel",24,"normal"))
        self.hideturtle()
        self.update_score()
    def game_over(self):
        self.goto(0,0)
        self.color("white")
        self.write("GAME OVER",move=False,align="center",font=("Ariel",24,"normal"))
    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_score()
    def update_score(self):
        self.write(f"Score: {self.score}",move=False,align="center",font=("Ariel",24,"normal"))
