#
# guess-my-number.py
# 
# A simple guessing game. The computer randomly generates 
# a number between 1 and 10. The user is prompted to continue guessing
# until they accurately guess the computer's number. They are told
# how many guesses it took to get the right number and are prompted
# to either continue playing or exit the game.

import random

playing = True

# We put the whole thing in a while loop so that the user 
# can play indefinitely if they wish.
while playing:
    pcNum = random.randrange(1, 11)
    guess = int(input("\nWelcome! Guess an integer between 1 and 10.\n> "))
    count = 0

    while guess != pcNum:
        count = count + 1

        if guess > pcNum:
            guess = int(input("Oops! You guessed too high. Try Again!\n> "))
        else:
            guess = int(input("Oops! You guessed too low. Try Again!\n> "))
    
    print("Congratulations! Your guess of {} was correct.\n".format(guess))
    print("It took you {} guesses.\n".format(count + 1))
    
    continuePlaying = input("Play again? (y/n)\n> ")

    while (continuePlaying != "y" and continuePlaying != "n"):
        print("You must enter either 'y' or 'n'.\n")
        continuePlaying = input("Play again? (y/n)\n> ")

    if continuePlaying == "n":
        playing = False

print("\nThanks for playing!\n")
