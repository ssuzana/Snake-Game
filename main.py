from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# create a new screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_on = True
while game_on:
    screen.update()  # refresh the screen
    time.sleep(0.3)  # adds 0.1 seconds delay
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
      food.refresh()
      snake.extend()
      scoreboard.update_score()

    # Detect collision with wall
    if snake.head.xcor() > 285 or snake.head.xcor() < - 285 or  snake.head.ycor() > 285 or  snake.head.ycor() < -285:
      scoreboard.reset()
      snake.reset()

    # Detect collision with tail
    for segment in snake.snake_segments[1:]:
      if snake.head.distance(segment) < 10:
        scoreboard.reset()
        snake.reset()

screen.exitonclick()