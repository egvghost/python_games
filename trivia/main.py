from question_model import Question
from data import trivia_data
from trivia import Trivia
from random import shuffle
from os import system

trivia_logo = '''
 _        _       _ 
| |      (_)     (_)
| |_ _ __ ___   ___  __ _ 
| __| '__| | \ / / |/ _` |
| |_| |  | |\ V /| | (_| |
 \__|_|  |_| \_/ |_|\__,_|
   
'''
system('clear')
print(trivia_logo)
categories = []
cat_nr = 0
nr_of_questions = 0
for q in trivia_data:
  if q["category"] not in categories:
    categories.append(q["category"])
print("Choose one category:")
for i in range(len(categories)):
  print(f"{i+1}) {categories[i]}")
while cat_nr not in range(1, len(categories)+1):
  cat_nr = int(input())
chosen_category = categories[cat_nr-1]
category_data = [item for item in trivia_data if item.get("category") == chosen_category]
cat_questions_nr = len(category_data)
print(f"Choose number of questions (1..{cat_questions_nr}): ")
while nr_of_questions not in range(1, cat_questions_nr+1):
  nr_of_questions = int(input())
question_bank = []
shuffle(category_data)
for q in category_data:
  question_bank.append(Question(q["question"], q["correct_answer"], q["incorrect_answers"]))
  if len(question_bank) == nr_of_questions:
    break
print(f"\n\033[1;35mSelection: Category '{chosen_category}' / Questions '{nr_of_questions}' \033[1;0m")
trivia = Trivia(question_bank)
while trivia.still_has_questions():
  trivia.show_question()

print(f"\033[1;33mYour score is: {str(trivia.score)}/{len(question_bank)} correct answers\n")