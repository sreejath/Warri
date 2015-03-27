__author__ = 'sreejath'
import sys
import math
import random
"""
Get validated number of games

"""
def getGames():
    n_games = 3
    selectGames = True
    print("Welcome to Rock, Paper Scissors.")
    while selectGames:

        try:
            n_games = int(input("Please enter the number of games you would like to play:"))
        except ValueError:
            print("Please enter an integer")
            continue

"""
Play game
"""
getGames()