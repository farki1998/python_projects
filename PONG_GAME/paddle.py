from turtle import Turtle, Screen

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5,1)
        self.penup()
        self.goto(position)
        #screen.listen()
        #screen.onkey(go_up,"Up")
        #screen.onkey(go_down,"Down")
    def go_up(self):
        new_y = self.ycor()+20
        self.goto(self.xcor(),new_y)
    def go_down(self):
        down_y = self.ycor()-20
        self.goto(self.xcor(),down_y)
