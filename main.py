import time
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from score import Score

# Screen Setup
screen = Screen()
screen.setup(width=600, height=600)
screen.listen()
screen.bgcolor('black')
screen.tracer(0)

snake_on = True
# Import necessary created classes
snake = Snake()
food= Food()
score = Score()

while snake_on:
    screen.update()
    time.sleep(.1)
    snake.move()
    # Detect collision with food
    if -30 + food.food.xcor() <= snake.tail[0].xcor() <= 30 + food.food.xcor() and -30 + food.food.ycor() <= snake.tail[0].ycor() <= 30 + food.food.ycor():
        food.room_shambles()
        score.point()
        snake.evolve()
    # Detect collision with tail
    for x in range(1, len(snake.tail)):
        if -19 + snake.tail[x].xcor()  <= snake.tail[0].xcor() <= 19 + snake.tail[x].xcor()  and -19 + snake.tail[x].ycor() <= snake.tail[0].ycor() <= 19 + snake.tail[x].ycor():
            score.reset()
            snake.reset()
    # Detect collision with wall
    if snake.tail[0].xcor() >= 290  or  snake.tail[0].xcor() <= -290 or snake.tail[0].ycor() <= -290 or snake.tail[0].ycor() >= 290:
        score.reset()
        snake.reset()


screen.exitonclick()