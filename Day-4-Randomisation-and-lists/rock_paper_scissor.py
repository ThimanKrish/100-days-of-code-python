# Rock, paper and scissor game.

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

options = [rock, paper, scissors]
user_selection = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(options[int(user_selection)])

computer_selection = random.randint(0, 2)
print("Computer chose:\n" + options[int(computer_selection)])

print(f"selection {user_selection} and {computer_selection}")
if user_selection == 0 and computer_selection == 0:
    print("Draw!")
if user_selection == 0 and computer_selection == 1:
    print("You lose!")
if user_selection == 0 and computer_selection == 2:
    print("You win!")
if user_selection == 1 and computer_selection == 0:
    print("You win!")
if user_selection == 1 and computer_selection == 1:
    print("Draw!")
if user_selection == 1 and computer_selection == 2:
    print("You lose!")
if user_selection == 2 and computer_selection == 0:
    print("You lose!")
if user_selection == 2 and computer_selection == 1:
    print("you win!")
if user_selection == 2 and computer_selection == 2:
    print("Draw!")