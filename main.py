from turtle import Screen
from snake import Snake  # Importing the Snake class from the snake module
from scoreboard import Score  # Importing the Score class from the scoreboard module
from food import Food  # Importing the Food class from the food module
import time

# Setup the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # Turn off screen updates

# Create food, snake, and scoreboard objects
food = Food()  # Create an instance of the Food class
snake = Snake()  # Create an instance of the Snake class
scoreboard = Score()  # Create an instance of the Score class

# Listen for keyboard inputs
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()  # Update the screen
    time.sleep(0.1)  # Pause for a short time to control the speed of the game
    snake.move()  # Move the snake

    # Detect food collision.
    if snake.head.distance(food) < 15:
        food.refresh()  # Refresh the food's position
        snake.extend()  # Extend the snake
        scoreboard.increase_score()  # Increase the score

    # Detect collision with walls.
    if (
        snake.head.xcor() > 280
        or snake.head.xcor() < -280
        or snake.head.ycor() > 280
        or snake.head.ycor() < -280
    ):
        game_is_on = False
        scoreboard.game_over()  # Display game over message

    # Detect collision with snake's own segments
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()  # Display game over message

screen.exitonclick()  # Close the screen when clicked
