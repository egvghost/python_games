import tkinter
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface():
  def __init__(self, quiz_brain: QuizBrain):
    self.quiz = quiz_brain

    self.window = tkinter.Tk()
    self.window.minsize(width=300, height=500)
    self.window.config(bg=THEME_COLOR)
    self.window.title("Quiz")
    
    self.canvas = tkinter.Canvas(width=300, height=250)
    self.canvas.config(bg="white")
    self.question_text = self.canvas.create_text(150, 125, text="placeholder text", font=("Arial", 20, "italic"), fill= THEME_COLOR, width=270)
    self.canvas.grid(row=2, column=2, columnspan=2, padx=20)
    
    self.label = tkinter.Label(text="Score: ", bg=THEME_COLOR)
    self.label.grid(row=1, column=3, pady=20)

    true_img = tkinter.PhotoImage(file="./images/true.png")
    false_img = tkinter.PhotoImage(file="./images/false.png")
    self.true_btn = tkinter.Button(image=true_img, highlightthickness=0, borderwidth=0, command=self.true_option)
    self.true_btn.grid(row=3, column=2, pady=20)
    self.false_btn = tkinter.Button(image=false_img, highlightthickness=0, borderwidth=0, command=self.false_option)
    self.false_btn.grid(row=3, column=3, pady=20)

    self.get_next_question()

    self.window.mainloop()

  def get_next_question(self):
    self.canvas.config(bg="white")
    self.label.config(text=f"Score: {self.quiz.score}")
    if self.quiz.still_has_questions():
      q_text = self.quiz.next_question()
      self.canvas.itemconfig(self.question_text, text=q_text)
    else:
      self.canvas.itemconfig(self.question_text, text="GAME OVER", font=("Courier",40,"bold"))
      self.true_btn.config(state=tkinter.DISABLED)
      self.false_btn.config(state=tkinter.DISABLED)

  def true_option(self):
      good_answer = self.quiz.check_answer("True")
      self.feedback(good_answer)

  def false_option(self):
      good_answer = self.quiz.check_answer("False")
      self.feedback(good_answer)

  def feedback(self, good_answer):
    if good_answer:
      self.canvas.config(bg="green")
    else:
      self.canvas.config(bg="red")
    self.canvas.after(500, func=self.get_next_question)
