# ---------------------------------------------------------*\
# Title: Guess the number (Main)
# Author: T. Maus (2022)
# ---------------------------------------------------------*/
# !/usr/bin/env python3
from functions import *

# Initialization
clear_screen()
print("Welcome to the Number Guessing Game!")

# Variables
is_on = True
guess_counter = 0

# Game-Loop
while is_on:
    print("I'm thinking of a number between 1 and 100.")
    
    computer_number = get_random_number()
    guess_counter = set_difficulty(computer_number)

    # Interaction-Loop ("Guessing")
    while guess_counter > 0:
        print(f"You have {guess_counter} attempts " +
              "remaining to guess the number.")

        # User guesses a number..
        try:
            guess = int(input("Make a guess: "))
        except TypeError:
            print("You should've entered a number, my friend. Try again")

        guess_counter -= 1

        # Check, if the number is correct
        if check_guess(guess, computer_number):
            print(f"You got it! The number was {guess}! 🏆")
            # os.system("say Congratulations! The test is now over")
            break
        elif guess_counter == 0:
            print("\nWhoa, you lost the game! 😈")
            print(f"My number was {computer_number}\n")
        else:
            continue

    # Asking, if the user wants to play another round..
    is_on = next_round()

print("Thank you for playing the game! 🎈")

# -------------------------Notes-----------------------------------------------*\
# The computer chooses a random number between 1 and 100, you have to guess!
# - Good luck! 🍀
# -----------------------------------------------------------------------------*
