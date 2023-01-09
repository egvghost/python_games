import random
from os import system

rps_logo = '''
                _                                                          _       
               | |                                                        (_)         
 _ __ ___   ___| | __         _ __   __ _ _ __   ___ _ __         ___  ___ _ ___ ___  ___  _ __ ___ 
| '__/ _ \ / __| |/ /        | '_ \ / _` | '_ \ / _ \ '__|       / __|/ __| / __/ __|/ _ \| '__/ __|
| | | (_) | (__|   <         | |_) | (_| | |_) |  __/ |          \__ \ (__| \__ \__ \ (_) | |  \__ \ 
|_|  \___/ \___|_|\_\        | .__/ \__,_| .__/ \___|_|          |___/\___|_|___/___/\___/|_|  |___/
                             | |         | |       
                             |_|         |_|       

         ___                          _____                                   ___
     __/  __\___                  __/  ____)_______                       __/  __\_________
           (____)                           _______)_                               _______)_
           (____)                           _________)                           ____________)
           (____)                           ________)                           (____)
     \_____(___)                  \______________)                        \_____(___)
'''

game = [
'''
      ___
  __/  __\___
        (____)
rock    (____)
        (____)
  \_____(___)
''',
'''
      _____
  __/  ____)_______
            _______)_
paper       _________)
            ________)
  \______________)
''',
'''
      ___
  __/  __\_________
            _______)_
scissors ____________)
        (____)
  \_____(___)
'''
]

while True:
  system('clear')
  your_choice = 0
  print(f"{rps_logo} \n")
  while your_choice not in ['1', '2', '3', 'q', 'Q']:
    your_choice = input("Make your choice: (1)rock - (2)paper - (3)scissors - (Q)quit\n")
  if your_choice.upper() == 'Q':
    break
  else:
    your_choice = int(your_choice)
    computer_choice = random.randint(1, 3)
    if (your_choice == 1 and computer_choice == 3) or \
      (your_choice == 2 and computer_choice == 1) or \
      (your_choice == 3 and computer_choice == 2):
      print(f"\nYour choice: {game[your_choice - 1]} \nComputer's choice: {game[computer_choice - 1]}\n\n*** YOU WON !! :) ***\n")
    elif your_choice == computer_choice:
      print(f"\nYour choice: {game[your_choice - 1]} \nComputer's choice: {game[computer_choice - 1]}\n\n*** DRAW :| ***\n")
    else:
      print(f"\nYour choice: {game[your_choice - 1]} \nComputer's choice: {game[computer_choice - 1]}\n\n*** YOU LOST :( ***\n")
    input("Press a key to continue..")