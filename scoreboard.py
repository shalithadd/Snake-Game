from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 15, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.hideturtle()
        self.penup()
        self.color('white')
        self.sety(270)
        self.get_high_score()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f'Score:  {self.score}  High Score:  {self.high_score}', align=ALIGNMENT,
                   font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()
        self.update_high_score()

    def update_high_score(self):
        with open('highscore.txt', mode='w') as f:
            f.write(str(self.high_score))

    def get_high_score(self):
        with open('highscore.txt', mode='r') as f:
            self.high_score = int(f.read())




