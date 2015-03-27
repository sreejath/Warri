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
                raise ValueError(
                    "To be fair, we need to play at least three games.\n Please enter an odd number that is three or higher.")
            if 0 == n_games % 2:
                raise ValueError(
                    "To determine a clear winner, we must play an odd number of games.\n Please enter an odd number that is three or higher.")
            selectGames = False
        except ValueError as v:
            print(v)
            continue


"""
Play game
"""
getGames()