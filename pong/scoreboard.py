from turtle import Turtle, Screen

TEXT_COLOR = "white"
ALIGNMENT = "center"
FONT = ("Courier", 70, "bold")
MAX_SCORE = 15

class Scoreboard(Turtle):

  def __init__(self):
    super().__init__()
    self.hideturtle()
    self.penup()
    self.color(TEXT_COLOR)
    self.goto(0, 280)
    self.p1_score = 0
    self.p2_score = 0
    self.winner = ''
  
  def update(self):
    self.clear()
    self.goto(0, 280)
    self._write(txt=f"{self.p1_score}  {self.p2_score}", align=ALIGNMENT, font=FONT)

  def increase(self, player):
    if player == 'p1':
      self.p1_score += 1
      if self.p1_score == MAX_SCORE:
        self.winner = "PLAYER 1"
    elif player == 'p2':
      self.p2_score += 1
      if self.p2_score == MAX_SCORE:
        self.winner = "PLAYER 2"
    self.update()
  
  def advantage(self, player):
    self.color('green')
    if player == 'p1':
      self.goto(-450, 330)
      self._write(txt=f"Stretch", align='left', font=('Courier', 20, 'normal'))
    elif player == 'p2':
      self.goto(450, 330)
      self._write(txt=f"Stretch", align='right', font=('Courier', 20, 'normal'))
    self.color(TEXT_COLOR)

  def game_over(self):
    self.goto(0,0)
    self._write(txt=f"    GAME OVER    {self.winner} wins", align=ALIGNMENT, font=("Courier", 30, "bold"))