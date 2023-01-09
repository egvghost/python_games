class Trivia:
  def __init__(self, question_list):
    self.question_nr = 0
    self.question_list = question_list
    self.score = 0
    print("\033[1;33mTrivia started \033[1;0m")

  def show_question(self):
    choice = 0
    print(f"\nQ.{self.question_nr + 1} {self.question_list[self.question_nr].question} \n")
    self.question_list[self.question_nr].shuffle_options()
    for i in range(1, len(self.question_list[self.question_nr].options)+1):
      print(f"{i}) {self.question_list[self.question_nr].options[i-1]} \n")
    while choice not in range(1, i+1):
      choice = int(input(f"Chose an option (1..{i}) "))
    self.check_answer(choice)
    self.question_nr += 1

  def check_answer(self, choice):
    print(f"The correct answer is \033[1;36m{self.question_list[self.question_nr].correct_answer} \033[1;0m", end = ' ')
    if self.question_list[self.question_nr].options[choice-1] == self.question_list[self.question_nr].correct_answer:
      print("\033[1;32m Well done!\n \033[1;0m")
      self.score += 1
    else:
      print("\033[1;31m You failed :(\n \033[1;0m")

  def still_has_questions(self):
    return self.question_nr < len(self.question_list)