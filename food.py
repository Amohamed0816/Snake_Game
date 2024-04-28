from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        # Initialize the food object
        super().__init__()
        self.shape("circle")  # Set the shape of the food to a circle
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # Stretch the circle to make it look like food
        self.color("blue")  # Set the color of the food to blue
        self.speed("fastest")  # Set the drawing speed to the fastest
        self.refresh()  # Generate a new position for the food

    def refresh(self):
        # Generate a new random position for the food
        x = random.randint(-280, 280)  # Random x-coordinate within the screen boundaries
        y = random.randint(-280, 280)  # Random y-coordinate within the screen boundaries
        self.goto(x, y)  # Move the food to the new random position
