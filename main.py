from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('Snake')
screen.tracer(0)

game_is_on = True
snake_body = []

snake = Snake()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.right, "Right")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")

food = Food(snake.snake_body)

while game_is_on:
    snake.move_forward()
    screen.update()
    time.sleep(0.1)

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh(snake.snake_body)
        snake.add_segment()
        scoreboard.increase_score()

    if snake.check_game_over():
        game_is_on = False
        scoreboard.write_game_over()

screen.exitonclick()
