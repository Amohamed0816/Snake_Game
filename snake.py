from turtle import Turtle

# Constants for the snake's initial positions, movement distance, and directions
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        # Initialize the snake's segments and create the snake
        self.segments = []
        self.create_snake()
        # Set the snake's head
        self.head = self.segments[0]

    def extend(self):
        # Extend the snake by adding a new segment to its tail
        self.add_segment(self.segments[-1].position())

    def add_segment(self, position):
        # Add a new segment to the snake at a given position
        new_body = Turtle(shape="square")
        new_body.penup()
        new_body.color("white")
        new_body.goto(position)
        self.segments.append(new_body)

    def create_snake(self):
        # Create the snake with segments at the starting positions
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def move(self):
        # Move the snake forward by one step
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        # Change the snake's direction to up if it's not currently moving down
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        # Change the snake's direction to down if it's not currently moving up
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        # Change the snake's direction to left if it's not currently moving right
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        # Change the snake's direction to right if it's not currently moving left
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
