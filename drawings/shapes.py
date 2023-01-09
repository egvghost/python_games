from turtle import Turtle, Screen

pen = Turtle()
screen = Screen()
colors = ['royal blue', 'light sea green', 'dark goldenrod', 'crimson', 'medium purple', 'steel blue', 'olive', 'dark magenta']
for i in range(3, 10):
  pen.color(colors[i-3])
  for _ in range(i):
    pen.forward(100)
    pen.right(360/i)

screen.exitonclick()