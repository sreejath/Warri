import math
import random
import time

def set_num_of_games():
    """
    Sets the number of games to be played.  We want an odd number of games,
    so we can have a winner.
    """

    # Set your finished flag.  Keep trying for a number until it's what we want.
    finished = False

    while not finished:

        num_of_games = input("How many games do you want to play?  "
                                 "Give me an odd number greater than 2! ")

        # Is it an number?
        try:

            # Try and convert answer into an int
            num_of_games = int(num_of_games)

        except:

            try:

                # If it's not an int, then check if it's a float
                float(num_of_games)
                print
                "That's not a whole number!  We need a whole number."
                continue

            except:

                # If it's not an int, and it's not a float, then it's text
                print
                "That's not a number at all!"
                continue

        # Is it an odd number?
        if num_of_games % 2 == 0:
            print
            "That's not an odd number!"
            continue

        # We want at least three games
        if num_of_games == 1:
            print
            "Come on, more than 2!"
            continue

        # If num_of_games is a lot, let's check to make sure the user wants to
        # keep playing that many games.
        if num_of_games > 15:

            # Set your False flag
            answer_valid = False

            while not answer_valid:
                answer = input("That's a lot of games! "
                                   "Are you sure you want to play that many? (yes or no) ")

                # If yes...
                if answer.lower() in ['yes', 'y']:

                    answer_valid = True

                # If no...
                elif answer.lower() in ['no', 'n']:

                    answer_valid = True


                # If something other than yes or not, try again.
                else:

                    print
                    'Not a valid answer  Sorry'
            answer_valid = False

        # If we've made it this far, then we've got a valid number of games
        finished = True

    # Now we need to calculate how many times it takes to win.
    # Divide num_of_games by 2 (we'll get X.5), then round up to find
    # out how many games the user has to win in order to win the whole game
    num_of_wins = int(math.ceil(num_of_games / 2.0))

    # Let's get started!
    print("Great!  Can you win %s out of %s games?" % (num_of_wins, num_of_games))

    # Return the results
    return num_of_wins, num_of_games


def rock_paper_scissors(num_of_wins, num_of_games):
    """
    The game itself.  After each win (or loss) we tally the results,
    and when you win or lose the game ends.
    Also, we need to have the ability to exit at any time.
    """

    # Establish scores
    computer_wins = 0
    user_wins = 0
    game_count = 0

    # Sleeps make it seem a bit more dramatic.  Why not?
    time.sleep(1)
    print('(Tip - at any time, type "options" to see available options.)')
    time.sleep(1)

    # Set your flag for the while loops
    game_finished = False

    # Game isn't finished, so we play on.
    while not game_finished:

        # Computer answers, then pick one at random and save it
        computer_answers = ['rock', 'paper', 'scissors']

        computer_answer = random.choice(computer_answers)

        # print "Hint - the computer's answer is %s." % computer_answer

        # Get the user's answer
        user_answer = input('Rock, Paper, or Scissors? ')

        # Set it to lowercase to make it easier to compare against
        user_answer = user_answer.lower()

        # In a real game, if both people have the same answer, it nullifies the round.
        # So here we just try again
        if user_answer == computer_answer:
            print ("Same answer, try again.")

        # Answer comparisons.  For each user answer, no matter who wins,
        # we increment that winner's score by one.  We also increment the
        # game count so we can track how long the same has been going on.

        # Rock
        elif user_answer == 'rock':

            game_count = game_count + 1

            if computer_answer == 'scissors':
                print("Computer's answer is %s.  You WIN this round!" % (computer_answer))
                user_wins = user_wins + 1

            elif computer_answer == 'paper':
                print("Computer's answer is %s.  You loose this round..." % (computer_answer))
                computer_wins = computer_wins + 1

        # Paper
        elif user_answer == 'paper':

            game_count = game_count + 1

            if computer_answer == 'rock':
                print ("Computer's answer is %s.  You WIN this round!" % (computer_answer))
                user_wins = user_wins + 1

            elif computer_answer == 'scissors':
                print ("Computer's answer is %s.  You loose this round..." % (computer_answer))
                computer_wins = computer_wins + 1

        # Scissors
        elif user_answer == 'scissors':

            game_count = game_count + 1

            if computer_answer == 'paper':
                print ("Computer's answer is %s.  You WIN this round!" % (computer_answer))
                user_wins = user_wins + 1

            elif computer_answer == 'rock':
                print ("Computer's answer is %s.  You loose this round..." % (computer_answer))
                computer_wins = computer_wins + 1

        # Also included is an options menu. Cleaner to not list these out each time,
        # but only show them when the user requests them
        elif user_answer == 'options':

            print ("'exit' - exit the game.")

            print ("'score' - tells you what the current score is.")
            print ("'count' - tells you what the game count is.")

        # Need to have the ability to exit
        elif user_answer == 'exit':

            # Set your False flag
            answer_valid = False

            # While the answer to "do i want to quit" is not valid, keep asking
            while not answer_valid:
                answer = input("Are you sure? (yes or no) ")

                # If yes...
                if answer.lower() in ['yes', 'y']:

                    # Exit this loop and set game_finished to true, ending the game
                    print ("Bye!")
                    game_finished = True
                    break

                # If no...
                elif answer.lower() in ['no', 'n']:

                    # Just exit this loop, and keep playing.
                    break

                # If something other than yes or not, try again.
                else:

                    print("Not a valid answer!  Sorry!")
                    answer_valid = False

        # What's the score?  Simple command here.
        elif user_answer == 'score':

            print("You: %s" % user_wins)
            print("CPU: %s" % computer_wins)

        # How long have we been playing?
        elif user_answer == 'count':

            print ("Playing game %s of %s." % (game_count + 1, num_of_games))

        # Finally, if we can't parse what the user gave, then try again.
        else:

            print("Not a valid answer!  Try again!")

        # If someone wins, end the game
        if user_wins == num_of_wins:

            print("You win!")

            print("Final score - You: %s, CPU %s." % (user_wins, computer_wins))
            break

        elif computer_wins == num_of_wins:

            print("You loose!")

            print("Final score - You: %s, CPU %s." % (user_wins, computer_wins))
            break

num_of_wins, num_of_games = set_num_of_games()

rock_paper_scissors(num_of_wins, num_of_games)