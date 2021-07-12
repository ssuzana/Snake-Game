from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 18, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as f:
            content = f.read()
        self.high_score = int(content)
        self.goto(0, 275)
        self.hideturtle()
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as f:
                f.write(str(self.high_score))

        self.score = 0
        self.update_scoreboard()

