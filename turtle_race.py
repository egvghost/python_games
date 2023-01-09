from turtle import Turtle, Screen
from random import randint, choice, shuffle

screen = Screen()
screen.title("Welcome to the Turtles race!! 🐢🐢🐢🐢🐢 🏁")

# define turtles
t1 = Turtle()
t2 = Turtle()
t3 = Turtle()
t4 = Turtle()
t5 = Turtle()

t1.shape('turtle')
t1.color('red')
t2.shape('turtle')
t2.color('green')
t3.shape('turtle')
t3.color('blue')
t4.shape('turtle')
t4.color('yellow')
t5.shape('turtle')
t5.color('purple')

turtles = [t1, t2, t3, t4, t5]
steps = [2, 4, 6, 8, 10]
shuffle(turtles)
pos = 200
for turtle in turtles:
  turtle.penup()
  turtle.setpos(-300, pos)
  pos -= 100

# Set goal-line
def goal():
  pen = Turtle()
  pen.penup()
  pen.setpos(310, -250)
  pen.pensize(3)
  pen.setheading(90)
  for pos in range(-25, 25):
    pen.pendown()
    pen.forward(5)
    pen.penup()
    pen.forward(5)
    pos += 10

  pen.forward(10)
  pen.pendown()
  pen.forward(40)
  pen.right(110)
  pen.forward(30)
  pen.right(140)
  pen.forward(30)
  pen.hideturtle()

def start_race():
  winner = []
  while not winner:
    for turtle in turtles:
      turtle.pendown()
      turtle.forward(choice(steps))
      if turtle.xcor() >= 300:
        winner.append(turtle.color()[0])
  print(f"Winner: {winner} - Your bet: '{bet}'")
  if bet in winner:
    print(f"You won!!")
  else:
    print(f"You lost :(")

goal()
global bet
bet = screen.textinput(title="Make your bet", prompt="Choose a turtle color:")
screen.listen()
screen.onkey(fun=start_race, key='space')

screen.exitonclick()