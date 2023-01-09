from turtle import Screen
from snake import Snake
from time import sleep
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("SNAKE GAME - Hit 'space' to start")
# Feed the snake and prevent it from biting its own tail!
screen.bgcolor("black")
screen.tracer(0)

def start_game():
  score = Scoreboard()
  score.update()
  while int(snake.head.xcor()) in range(-285, 285) and int(snake.head.ycor()) in range(-285, 285):
    screen.onkey(fun=snake.up, key='Up')
    screen.onkey(fun=snake.down, key='Down')
    screen.onkey(fun=snake.right, key='Right')
    screen.onkey(fun=snake.left, key='Left')
    sleep(0.2)
    snake.move()
    if snake.head.distance(food) < 15:
      score.increase()
      snake.grow()
      food.move()
    screen.update()
    # Detect collision with tail
    for segment in snake.segments[1:]:
      collision = False
      if snake.head.distance(segment) < 10:
        collision = True
        break
    if collision:
      break
  print("collision detected")
  score.game_over()

snake = Snake()
food = Food()
screen.update()
screen.listen()
screen.onkey(fun=start_game, key='space')
screen.exitonclick()