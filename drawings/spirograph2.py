from turtle import Turtle, Screen, colormode
from random import randint

pen = Turtle()
pen.speed('fastest')
screen = Screen()
colormode(255)

def random_color():
  r = randint(0, 255)
  g = randint(0, 255)
  b = randint(0, 255)
  return (r, g, b)

for _ in range(24):
  pen.color(random_color())
  pen.circle(100, 45, 20)
  pen.color(random_color())
  pen.circle(30, 360, 20)
  pen.right(150)

screen.exitonclick()