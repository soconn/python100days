rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
ROCK
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
PAPER
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
SCISSORS
'''


#Write your code below this line 👇
import random

temp = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
choice = int(temp)
if (choice > 2):
    print("you're a terrible person!")
    exit


def number_function():
    if hand==0:
        print(rock)
    elif hand==1:
        print(paper)
    else:
        print(scissors)

hand=choice
print(". . . HUMAN")
number_function()

opponent = random.randint(0, 2)
hand=opponent
print(". . . ROBOT")
number_function()

if choice == 0:
    if opponent == 0:
        print("It's a DRAW!!!")
    elif opponent == 1:
        print("PAPER beats ROCK - you LOSE!")
    else:
        print("ROCK beats SCISSORS - you WIN!")
elif choice == 1:
    if opponent == 0:
        print("PAPER beats ROCK - you WIN!")
    elif opponent == 1:
        print("It's a DRAW!!!")
    else:
        print("SCISSORS beats PAPER - you LOSE!")
else:
    if opponent == 0:
        print("ROCK beats SCISSORS - you LOSE!")
    elif opponent == 1:
        print("SCISSORS beats PAPER - you WIN!")
    else:
        print("It's a DRAW!!!")