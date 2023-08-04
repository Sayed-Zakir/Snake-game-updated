from turtle import Turtle

ALLIGN="center"
FONT=("Arial",12,"normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.color("white")
        self.score=0
        with open("c:/Users/zakir/Downloads/Python for days/Snake game - Copy/data.txt") as data:
            self.highscore=int(data.read())
        self.write(f"Score: {self.score}",align="center",font=("Arial",12,"normal"))

    def reset(self):
        if self.score>self.highscore:
            self.highscore=self.score
            with open("c:/Users/zakir/Downloads/Python for days/Snake game - Copy/data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.score=0
        self.update_score()


    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}  Highscore: {self.highscore}",align=ALLIGN,font=FONT)

    def increase_score(self):
        self.score+=1
        self.update_score()
        

