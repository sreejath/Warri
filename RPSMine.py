__author__ = 'sreejath'
import random

"""
Get validated number of games

"""


def get_games():
    """
    This subroutine gets the number of games the user wants to play.
    It then validates that this is an odd number 3 or higher.
    """
    n_games = 3
    select_games = True
    print("Welcome to Rock, Paper Scissors.")
    while select_games:

        try:
            n_games = int(input("Please enter the number of games you would like to play:"))

            if n_games < 3:
                raise ArithmeticError(
                    "To be fair, we need to play at least three games.\n"
                    "Please enter an odd number that is three or higher.")
            if 0 == n_games % 2:
                raise ArithmeticError(
                    "To determine a clear winner, we must play an odd number of games.\n"
                    "Please enter an odd number that is three or higher.")
            select_games = False
        except ValueError:
            print("Please enter an odd number greater than or equal to 3.")
            continue
        except ArithmeticError as a:
            print(a)
            continue
    return n_games


# noinspection PyPep8Naming
def playRPS(n_games):
    user_score = 0
    computer_score = 0
    game_counter = 0
    winner = ""
    choices = ["rock", "paper", "scissors"]
    game_finished = False
    while not game_finished:
        user_choice = input("Rock, Paper, Scissors?").lower()
        computer_choice = random.choice(choices)
        if computer_choice == user_choice:
            print("Computer chose %s as well.\n"
                  "Please try again." % user_choice)

        # User chose Rock
        elif user_choice == "rock":
            if computer_choice == "paper":
                user_score += 1
                print("You win this round")
                if user_score > (n_games / 2):
                    winner = "You win!"
                    break
            else:
                computer_score += 1
                print("The computer wins this round")
                if computer_score > (n_games / 2):
                    winner = "The Computer wins!"
                    break
            game_counter += 1
            if game_counter >= n_games:
                break
            print("You: %d - Computer: %d" % (user_score, computer_score))

        # User chose Paper

        elif user_choice == "paper":
            if computer_choice == "rock":
                user_score += 1
                print("You win this round")
                if user_score > (n_games / 2):
                    winner = "You win!"
                    break
            else:
                computer_score += 1
                print("The computer wins this round")
                if computer_score > (n_games / 2):
                    winner = "The Computer wins!"
                    break
            game_counter += 1
            if game_counter >= n_games:
                break
            print("You: %d - Computer: %d" % (user_score, computer_score))

        # User chose Scissors
        elif user_choice == "scissors":
            if computer_choice == "paper":
                user_score += 1
                print("You win this round")
                if user_score > (n_games / 2):
                    winner = "You win!"
                    break
            else:
                computer_score += 1
                print("The computer wins this round")
                if computer_score > (n_games / 2):
                    winner = "The Computer wins!"
                    break
            game_counter += 1
            if game_counter >= n_games:
                break
            print("You: %d - Computer: %d" % (user_score, computer_score))
        elif user_choice == "q":
            user_choice = input("Are you sure you want to quit (y/n)?\n"
                                "You have %d games remaining." % (n_games-game_counter))
            if user_choice == "y":
                winner = "Loser, I mean user chose to quit!"
                break
            else:
                continue
        else:
            print("Invalid choice. Please type Rock, Paper or Scissors")
            continue
    print("Final Score :- You:%d - Computer:%d. %s" % (user_score, computer_score, winner))

"""
Play game
"""
playRPS(get_games())