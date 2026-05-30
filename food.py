from turtle import Turtle
import random
class Food:
    def __init__(self):
        self.food = Turtle()
        self.food.penup()
        self.food.shape('circle')
        self.food.color('purple')
        self.food.shapesize(.5, .5, 1)
        self.food.goto(x=random.randint(0,250), y=random.randint(0, 250))

	# Function that teleports food item to a random location every time it is 'touched' by the snake
    def room_shambles(self):
        self.food.teleport(x=random.randint(0,250), y=random.randint(0, 250))
