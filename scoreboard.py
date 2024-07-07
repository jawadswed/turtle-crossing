from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(-280, 260)
        self.level = 0
        self.show_level()

    def show_level(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def update_level(self):
        self.level += 1
        self.show_level()

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"Game Over", align="Center", font=FONT)
