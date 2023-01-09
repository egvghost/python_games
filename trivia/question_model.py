from random import shuffle

class Question:
  def __init__(self, question, correct_answer, incorrect_answers):
    self.question = question
    self.correct_answer = correct_answer
    self.options = [correct_answer] + incorrect_answers

  def shuffle_options(self):
    shuffle(self.options)
