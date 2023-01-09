from turtle import Turtle, Screen
from random import randint, choice, shuffle

screen = Screen()
screen.title("Welcome to the Turtles race!! 🐢🐢🐢🐢🐢 🏁 - Hit 'space' to start")

# Set running_track
def running_track():
  pen = Turtle()
  pen.speed('fastest')
  pen.penup()
  track_lines = [250, 150, 50, -50, -150, -250]
  for line in track_lines:
    pen.setpos(-300, line)
    while pen.xcor() < 280:
      pen.pendown()
      pen.forward(5)
      pen.penup()
      pen.forward(5)
  pen.hideturtle()

# Set goal_line
def goal_line():
  pen = Turtle()
  pen.speed('fastest')
  pen.penup()
  pen.setpos(280, -250)
  pen.pensize(3)
  pen.setheading(90)
  for pos in range(-25, 25):
    pen.pendown()
    pen.forward(5)
    pen.penup()
    pen.forward(5)
    pos += 10

  pen.hideturtle()
  pen.forward(10)
  pen.pendown()
  pen.forward(53)
  xpos = pen.xcor()
  ypos = pen.ycor()
  pen.setpos(xpos, ypos - 3)
  pen.right(90)
  pen.forward(43)
  pen.right(90)
  pen.forward(25)
  pen.right(90)
  pen.forward(43)
  pen.penup()
  pen.pensize(6)
  pen.right(90)
  pen.forward(2)
  pen.right(90)
  for n in range(5):
    for i in range(3):
      pen.forward(10)
      pen.pendown()
      pen.forward(4)
      pen.penup()
    xpos = pen.xcor()
    ypos = pen.ycor()
    pen.setpos(xpos, ypos + 5)
    pen.setheading(180 * (n + 1))
    pen.forward(-3)

# Set race parameters
def start_race():
  winner = []
  while not winner:
    for turtle in turtles:
      turtle.pendown()
      turtle.forward(choice(steps))
      if turtle.xcor() > 267:
        winner.append(turtle.color()[0])
  print(f"Winner: {winner} - Your bet: '{bet}'")
  if bet in winner:
    print(f"You won!!")
  else:
    print(f"You lost :(")

# running_track()
goal_line()

# Define turtles
turtles = []
colors = ['red', 'green', 'blue', 'yellow', 'purple']
positions = [200, 100, 0, -100, -200]
steps = range(1, 10)
shuffle(colors)
for i in range(5):
  turtle = Turtle(shape='turtle')
  turtle.speed('fast')
  turtle.color(colors[i])
  turtle.penup()
  turtle.setpos(-300, positions[i])
  turtles.append(turtle)
  i += 1

global bet
bet = screen.textinput(title="Make your bet", prompt="Choose a turtle color:")
screen.listen()
screen.onkey(fun=start_race, key='space')

screen.exitonclick()