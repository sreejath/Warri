__author__ = 'sreejath'
import sys
import math
import random

"""
Get validated number of games

"""


def getGames():
    """


    """
    n_games = 3
    selectGames = True
    print("Welcome to Rock, Paper Scissors.")
    while selectGames:

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
            selectGames = False
        except ValueError as v:
            print("Please enter an odd number greater than or equal to 3.")
            continue
        except ArithmeticError as a:
            print(a)
            continue
    return n_games


def playRPS(nGames):

    user_choice = ""
    computer_choice = ""
    user_score = 0
    computer_score = 0
    game_counter = 0
    choices = ["rock", "paper", "scissors"]
    game_finished = False
    while not game_finished:
        user_choice = input("Rock, Paper, Scissors?").lower()
        computer_choice = random.choice(choices)
        if computer_choice==user_choice:
            print("Computer chose %s as well.\n"
                  "Please try again." % user_choice.capitalize())
        elif user_choice == "rock":
            if computer_choice=="paper":
                user_score += 1
                print("You win")
                if user_score > (nGames/2):
                    break
            else:
                computer_score += 1
                print("The computer wins")
                if computer_score > (nGames/2):
                    break
            game_counter += 1
            if game_counter >= nGames:
                break
            print("You: %d - Computer: %d" % (user_score, computer_score))

"""
Play game
"""
playRPS(getGames())
