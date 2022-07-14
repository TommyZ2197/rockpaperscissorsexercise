


#
# FYI: this is to satisfy the OPTIONAL testing challenge objectives
# ... https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/testing_challenges.md
#

from game import determine_winner


def test_determination_of_the_winner():

    assert determine_winner("rock", "rock") == "Tie!"
    assert determine_winner("rock", "paper") == "paper"
    assert determine_winner("rock", "scissors") == "rock"

    assert determine_winner("paper", "rock") == "paper"
    assert determine_winner("paper", "paper") == "Tie!"
    assert determine_winner("paper", "scissors") == "scissors"

    assert determine_winner("scissors", "rock") == "rock"
    assert determine_winner("scissors", "paper") == "scissors"
    assert determine_winner("scissors", "scissors") == "Tie!"
