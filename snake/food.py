from turtle import Turtle
from random import choice

FOOD_COLOR = "purple"
FOOD_SHAPE = "circle"
POSITIONS = list(range(-280, 300, 20))

class Food(Turtle):

    def __init__(self):
      super().__init__()
      self.penup()
      self.color(FOOD_COLOR)
      self.shape(FOOD_SHAPE)
      self.shapesize(0.5)
      self.move()

    def move(self):
      self.goto(choice(POSITIONS), choice(POSITIONS))