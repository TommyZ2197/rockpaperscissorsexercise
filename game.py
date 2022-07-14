#this is the "game.py" file
import random


#
# todo: write some Python code here to satisfy the exercise objectives
# ... https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md
#USER INPUTS
print("Welcome Player One to Rock, Paper, Scissors, Shoot!")
player_choice = input("Please make a selection ('Rock', 'Paper', 'Scissors'):")
player_choice = player_choice.lower()

print(f"You chose:, '{player_choice}' ")

#Validate user inputs
valid_options = ["rock", "paper", "scissors"]
if player_choice not in valid_options:
    print("Sorry, please come back and try again")
    exit ()
#computer choice
valid_options = ["rock", "paper", "scissors"]
computer_choice = random.choice(valid_options)
print("Computer chose:", computer_choice)

#Determine the winner
winner = {'scissors':'rock', 'rock':'paper', 'paper':'scissors'} 
if player_choice == computer_choice:
    print("TIE")
elif player_choice == winner[computer_choice]:
    print ("Amazing, you won!")
elif computer_choice == winner[player_choice]:
    print("Computer wins :( ")

print("Thank you for playing! See you soon!)")






