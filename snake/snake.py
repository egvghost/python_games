from turtle import Turtle
from time import sleep

SNAKE_COLOR = "green"
SNAKE_SHAPE = "square"
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Snake:

  def __init__(self):
    self.segments = []
    self.create()
    self.head = self.segments[0]

  def create(self):
    for i in range(3):
      position = (-20 * i, 0)
      self.add_segment(position)

  def add_segment(self, position):
    segment = Turtle()
    segment.penup()
    segment.color(SNAKE_COLOR)
    segment.shape(SNAKE_SHAPE)
    segment.goto(position)
    self.segments.append(segment)

  def grow(self):
    self.add_segment(self.segments[-1].position())

  def move(self):
    for i in range(len(self.segments) -1, 0, -1):
      new_xpos = self.segments[i-1].xcor()
      new_ypos = self.segments[i-1].ycor()
      self.segments[i].goto(new_xpos, new_ypos)
    self.head.forward(MOVE_DISTANCE)

  def up(self):
    if self.head.heading() != DOWN:
      self.head.setheading(UP)
  
  def down(self):
    if self.head.heading() != UP:
      self.head.setheading(DOWN)

  def right(self):
    if self.head.heading() != LEFT:
      self.head.setheading(RIGHT)
  
  def left(self):
    if self.head.heading() != RIGHT:
      self.head.setheading(LEFT)
