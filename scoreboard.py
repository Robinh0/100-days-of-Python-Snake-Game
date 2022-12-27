from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 12, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.write_score()

    def write_score(self):
        self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write_score()

    def write_game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align=ALIGNMENT, font=FONT)
