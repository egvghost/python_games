'''
    Rules:
      Try to guess the hidden 5 digit number.
      Each attempt will provide the amount of (G)ood, (R)egular and (B)ad digits, acording to:
        (G)ood: the digit exists in the hidden number and is in the right position.
        (R)egular: the digit exists in the hidden number but IS NOT in the right position.
        (B)ad: the digit DOES NOT exist in the hidden number
'''

import random
from os import system

numberle_logo = '''
                       _                _   
                      | |              | |   
 _ __  _   _ _ __ ___ | |__   ___ _ __ | | ___ 
| '_ \| | | | '_ ' _ \| '_ \ / _ \ '__/| |/ _ \ 
| | | | |_| | | | | | | |_) |  __/ |   | |  __/
|_| |_|\__,_|_| |_| |_|_.__/ \___|_|   |_|\___|

'''

hidden_number = []
for nun in range(5):
  random_digit = str(random.randint(0, 9))
  while random_digit in hidden_number:
    random_digit = str(random.randint(0, 9))
  hidden_number.append(str(random_digit))

your_number = ''
good, regular, bad = 0, 0, 0
attempts = []

while your_number != ''.join(hidden_number):
  system('clear')
  print(numberle_logo)
  if (good + regular + bad) > 0:
    attempts.append(f"Your guess for {your_number}: {good} (G), {regular} (R), {bad} (B)\n")
  for item in attempts:
    print(item)
  good, regular, bad = 0, 0, 0
  your_number = input("Guess the hidden 5 digit number: ")
  while not your_number.isdigit() or len(your_number) != 5:
    your_number = input("Guess the hidden 5 digit number: ")
  for item in range(5):
    if your_number[item] == hidden_number[item]:
      good += 1
    elif your_number[item] in hidden_number:
      regular += 1
    else:
      bad += 1

print(f"\n** YOU WON !! :) -> {your_number}")