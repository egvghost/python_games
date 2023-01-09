from turtle import Turtle, Screen, colormode
from random import choice,randint

pen = Turtle()
screen = Screen()
screen.title("Random walk 🔀 🚶🏾‍♂️")
pen.pensize(3)
colormode(255)
angles = [0, 90, 180, 270]

def random_color():
  r = randint(0, 255)
  g = randint(0, 255)
  b = randint(0, 255)
  return (r, g, b)

for _ in range(300):
  pen.color(random_color())
  pen.right(choice(angles))
  pen.forward(30)

screen.exitonclick()