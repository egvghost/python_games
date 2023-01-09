from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

TOP_LIMIT = 380
BOTTOM_LIMIT = -380
LEFT_LIMIT = -450
RIGHT_LIMIT = 450

screen = Screen()
screen.setup(width=1000, height=800)
screen.title("PONG GAME - Hit 'space' to start")
screen.bgcolor("black")
screen.tracer(0)

def start_game():
  score = Scoreboard()
  score.update()
  p1_adv = 0
  p2_adv = 0
  while not score.winner:
    screen.onkey(fun=p1_paddle.move_up, key='a')
    screen.onkey(fun=p1_paddle.move_down, key='z')
    screen.onkey(fun=p2_paddle.move_up, key='Up')
    screen.onkey(fun=p2_paddle.move_down, key='Down')
    screen.update()
    ball.move()
    # Detect collision with walls
    if ball.ycor() >= TOP_LIMIT or ball.ycor() <= (BOTTOM_LIMIT + 10):
      ball.bounce_y()
    # Detect collision with paddle
    if ball.xcor() > (RIGHT_LIMIT - 15) or ball.xcor() < (LEFT_LIMIT + 15):
      if ball.distance(p1_paddle.pos()) < 50 or ball.distance(p2_paddle.pos()) < 50:
        ball.bounce_x()
    # Detect score
    if ball.xcor() > (RIGHT_LIMIT + 40):
      score.increase('p1')
      p1_adv +=1
      p2_adv = 0
      p2_paddle.shrink()
      ball.reset_pos('p2')
      p2_paddle.reset_pos(RIGHT_LIMIT)
      screen.update()
    elif ball.xcor() < (LEFT_LIMIT - 40):
      score.increase('p2')
      p2_adv +=1
      p1_adv = 0
      p1_paddle.shrink()
      ball.reset_pos('p1')
      p1_paddle.reset_pos(LEFT_LIMIT)
      screen.update()
    # Stretch/Shrink paddle on advantage
    if p1_adv >= 5:
      p1_paddle.stretch()
      p1_adv = 0
      p2_paddle.shrink()
      score.advantage('p1')
    elif p2_adv >= 5:
      p2_paddle.stretch()
      p2_adv = 0
      p1_paddle.shrink()
      score.advantage('p2')
  score.game_over()

field = Turtle()
field.hideturtle()
field.penup()
field.color('white')
field.goto(0, -400)
field.setheading(90)
for _ in range(80):
  field.forward(5)
  field.penup()
  field.forward(5)
  field.pendown()
p1_paddle = Paddle(xpos=LEFT_LIMIT)
p2_paddle = Paddle(xpos=RIGHT_LIMIT)
ball = Ball()
screen.update()
screen.listen()
screen.onkey(fun=start_game, key='space')
screen.exitonclick()