from turtle import Turtle
from random import choice

BALL_COLOR = "cyan"
BALL_SHAPE = "circle"
START_XPOS = [-432, 432]
TOP_LIMIT = 380
BOTTOM_LIMIT = -380
INITIAL_STEPS = 3

class Ball(Turtle):

  def __init__(self):
    super().__init__()
    self.penup()
    self.color(BALL_COLOR)
    self.shape(BALL_SHAPE)
    self.shapesize(0.5)
    self.goto(choice(START_XPOS), 0)
    self.steps = INITIAL_STEPS
    self.y_move = self.steps
    if self.xcor() < 0:
      self.x_move = self.steps * 1
    else:
      self.x_move = self.steps * -1

  def move(self):
    self.x_move = self.x_move / abs(self.x_move) * self.steps
    self.y_move = self.y_move / abs(self.y_move) * self.steps
    self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)
  
  def bounce_y(self):
    self.y_move *= -1
  
  def bounce_x(self):
    self.x_move *= -1
    self.steps *= 1.1

  def reset_pos(self, player):
    self.steps = INITIAL_STEPS
    self.y_move = self.steps
    if player == 'p1':
      self.x_move = self.steps
      self.goto(START_XPOS[0], 0)
    elif player == 'p2':
      self.x_move = self.steps * -1
      self.goto(START_XPOS[1], 0)
