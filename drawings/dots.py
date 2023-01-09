from turtle import Turtle, Screen, colormode
from random import randint

pen = Turtle()
pen.speed('fast')
screen = Screen()
colormode(255)

def random_color():
  r = randint(0, 255)
  g = randint(0, 255)
  b = randint(0, 255)
  return (r, g, b)

pen.penup()
for i in range(20):
  pen.setpos(-300, 300 - i*30)
  for _ in range(30):
    pen.color(random_color())
    pen.pendown()
    pen.dot(10)
    pen.penup()
    pen.forward(20)

screen.exitonclick()