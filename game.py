#this is the "game.py" file
import random
import game

#
# todo: write some Python code here to satisfy the exercise objectives
def determine_winner(player_choice, computer_choice):
    champions = {'rock':'scissors', 'paper':'rock', 'scissors':'paper'}
    ##Determines the winning choice between two valid choices from selectable options: "rock", "paper", or "scissors".
    lossers = champions[player_choice]
    if player_choice == computer_choice:
        Print('None')
    elif player_choice in champions:
        print(f"{player_choice}")
    elif player_choice in lossers:
        print(f"{computer_choice}")

    ##Example: determine_winner("rock", "paper")
    

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
#removed else:continue  
#computer choice
valid_options = ["rock", "paper", "scissors"]
computer_choice = random.choice(valid_options)
print("Computer chose:", computer_choice)

#Determine the winner
winner = {'scissors':'rock', 'rock':'paper', 'paper':'scissors'} 
if player_choice == computer_choice:
    print("Tie!")
elif player_choice == winner[computer_choice]:
    print ("Amazing, you won!")
elif computer_choice == winner[player_choice]:
    print("Computer wins :( ")

print("Thank you for playing! See you soon!")






