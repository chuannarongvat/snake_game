from turtle import Turtle
ALINGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.increase_score()
    
    def increase_score(self):
        self.reset()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.speed("fastest")

        self.write(f"Score: {self.score}", True, align=ALINGNMENT, font=FONT)
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over.", True, align=ALINGNMENT, font=FONT)

        