from turtle import Turtle, Screen

screen = Screen()
pen = Turtle()

screen.listen()

def pen_down():
  pen.pendown()

def pen_up():
  pen.penup()

def turn_right():
  pen.right(10)

def turn_left():
  pen.left(10)

def draw_fwrd():
  pen.forward(10)

def draw_bwrd():
  pen.back(10)

def draw_right():
  pen.setheading(0)
  pen.forward(10)

def draw_left():
  pen.setheading(180)
  pen.forward(10)

def draw_up():
  pen.setheading(90)
  pen.forward(10)

def draw_down():
  pen.setheading(270)
  pen.forward(10)

def draw_circle():
  pen.circle(50, 10, 10)

def delete():
  pen.clear()
  pen.penup()
  pen.home()
  pen.pendown()

screen.onkey(fun=draw_right, key='Right')
screen.onkey(fun=draw_left, key='Left')
screen.onkey(fun=draw_up, key='Up')
screen.onkey(fun=draw_down, key='Down')
screen.onkey(fun=turn_right, key='r')
screen.onkey(fun=turn_left, key='l')
screen.onkey(fun=draw_fwrd, key='f')
screen.onkey(fun=draw_bwrd, key='b')
screen.onkey(fun=draw_circle, key='c')
screen.onkey(fun=pen_down, key= 'z')
screen.onkey(fun=pen_up, key='a')
screen.onkey(fun=delete, key='d')

screen.exitonclick()