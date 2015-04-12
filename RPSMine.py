__author__ = 'sreejath'
import random


def get_games():

    """
    This subroutine gets the number of games the user wants to play.
    It then validates that this is an odd number 3 or higher.
    """
    n_games = 3  # Initialized to 3, because, well why not?
    select_games = True  # Boolean to control the while loop
    print("Welcome to Rock, Paper Scissors.\n"
          "Type 'o' at any time to see game options\n"
          "Type 'q' at any time to quit the game'")
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
                  "Please try again." % user_choice.capitalize())

        # User chose Rock
        elif "rock" == user_choice:
            if computer_choice == "scissors":
                user_score += 1
                print("The computer chose Scissors. You win this round")
                if user_score > (n_games / 2):
                    winner = "You win!"
                    break
            else:
                computer_score += 1
                print("The computer chose Paper. The computer wins this round")
                if computer_score > (n_games / 2):
                    winner = "The Computer wins!"
                    break
            game_counter += 1
            if game_counter >= n_games:
                break
            print("You: %d - Computer: %d" % (user_score, computer_score))

        # User chose Paper

        elif "paper" == user_choice:
            if computer_choice == "rock":
                user_score += 1
                print("The Computer chose Rock. You win this round")
                if user_score > (n_games / 2):
                    winner = "You win!"
                    break
            else:
                computer_score += 1
                print("The Computer chose Scissors. The computer wins this round")
                if computer_score > (n_games / 2):
                    winner = "The Computer wins!"
                    break
            game_counter += 1
            if game_counter >= n_games:
                break
            print("You: %d - Computer: %d" % (user_score, computer_score))

        # User chose Scissors
        elif "scissors" == user_choice:
            if computer_choice == "paper":
                user_score += 1
                print("The Computer chose Paper. You win this round")
                if user_score > (n_games / 2):
                    winner = "You win!"
                    break
            else:
                computer_score += 1
                print("The Computer chose Rock. The computer wins this round")
                if computer_score > (n_games / 2):
                    winner = "The Computer wins!"
                    break
            game_counter += 1
            if game_counter >= n_games:
                break
            print("You: %d - Computer: %d" % (user_score, computer_score))
        elif "q" == user_choice:
            user_quit = False
            while not user_quit:
                user_choice = input("WHAT?!!! Are you sure you want to quit (y/n)?\n"
                                    "You have %d games remaining." % (n_games-game_counter)).lower()
                if user_choice == "y" or user_choice == "yes":
                    winner = "Loser, I mean user chose to quit!"
                    game_finished = True
                    break
                elif user_choice == "n" or user_choice == "no":
                    break
                else:
                    print("Invalid choice. Please type yes/no (or y/n)")
                    continue
        elif "o" == user_choice:
            in_options = True
            while in_options:
                selected_option = input("Press 's' to see current score\n"
                                        "Press 'q' to quit the game\n"
                                        "Press 'b' to go back to the game")

                if 's' == selected_option:
                    print("The current score is You %d - Computer %d %d games out of %d remain"
                          % (user_score, computer_score, (n_games-computer_score-user_score), n_games))
                    continue
                elif "b" == selected_option:
                    break
                else:
                    print("Not implemented yet")
                    break

        else:
            print("Invalid choice. Please type Rock, Paper or Scissors")
            continue
    print("Final Score :- You:%d - Computer:%d. %s" % (user_score, computer_score, winner))


"""
Play game
"""
playRPS(get_games())