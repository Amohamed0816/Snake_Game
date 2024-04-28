from turtle import Turtle

# Constants for text alignment and font
ALIGNMENT = 'Center'
FONT = ('Courier', 20, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        # Initialize the score display
        self.score_title()

    def score_title(self):
        # Display the initial score at the top of the screen
        self.goto(0, 270)
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        # Increase the score by 1 and update the score display
        self.score += 1
        self.clear()
        self.score_title()

    def game_over(self):
        # Display "Game Over" message at the center of the screen
        self.goto(0, 0)
        self.write("Game Over", False, ALIGNMENT, FONT)
