from turtle import Turtle

PADDLE_COLOR = "white"
PADDLE_SHAPE = "square"
MOVE_DISTANCE = 20
WIDTH = 1
LENGTH = 4
TOP_LIMIT = 400
BOTTOM_LIMIT = -400

class Paddle(Turtle):

  def __init__(self, xpos):
    super().__init__()
    self.xpos = xpos
    self.penup()
    self.setheading(90)
    self.shape(PADDLE_SHAPE)
    self.shapesize(stretch_wid=WIDTH, stretch_len=LENGTH)
    self.color(PADDLE_COLOR)
    self.goto(xpos, 0)
    self.length = LENGTH

  def stretch(self):
    self.length += 1
    self.shapesize(stretch_wid=WIDTH, stretch_len=self.length)

  def shrink(self):
    self.length = LENGTH
    self.shapesize(stretch_wid=WIDTH, stretch_len=self.length)

  def move_up(self):
    if self.ycor() <= TOP_LIMIT - (LENGTH * 20):
      self.ypos = self.ycor() + MOVE_DISTANCE
      self.goto(self.xpos, self.ypos)
  
  def move_down(self):
    if self.ycor() >= BOTTOM_LIMIT + (LENGTH * 20):
      self.ypos = self.ycor() - MOVE_DISTANCE
      self.goto(self.xpos, self.ypos)

  def reset_pos(self, xpos):
      self.goto(xpos, 0)
