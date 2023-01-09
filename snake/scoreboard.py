from turtle import Turtle, Screen

TEXT_COLOR = "white"
ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")

class Scoreboard(Turtle):

  def __init__(self):
    super().__init__()
    self.hideturtle()
    self.penup()
    self.color(TEXT_COLOR)
    self.goto(0, 280)
    self.score = 0
  
  def update(self):
    self.clear()
    self._write(txt=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

  def increase(self):
    self.score += 1
    self.update()

  def game_over(self):
    self.goto(0,0)
    self._write(txt="GAME OVER", align=ALIGNMENT, font=("Courier", 30, "bold"))