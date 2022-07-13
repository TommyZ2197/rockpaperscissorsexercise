
import random


#
# todo: write some Python code here to satisfy the exercise objectives
# ... https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md
#USER INPUTS
print("Welcome to Rock Paper Scissors")
user_choice = input("Please make a selection ('Rock', 'Paper', 'Scissors'):")
print(f"You chose:, '{user_choice}' ")

#computer choice
valid_options = ["rock", "paper", "scissors"]
computer_choice = random.choice(valid_options)
print("Computer chose:", computer_choice)
