# ---------------------------------------------------------*\
# Title: Functions
# Author: T. Maus (2022)
# ---------------------------------------------------------*/
#!/usr/bin/env python3
import os
import random
from art import logo


def clear_screen():
    """Provide the clean startup console with logo"""
    os.system("clear")
    print(logo)


def get_random_number():
    """Set the initial random number"""
    rand_int = random.randint(1, 100)
    return rand_int


def set_difficulty(cheat):
    """Set the level of difficulty"""
    while True:
        level = input("\nChoose a difficulty. Type 'easy' or 'hard': ")
        level = str(level).lower()

        if level == "easy":
            return 10
        elif level == "hard":
            return 5
        elif level == "tip":
            print (f"Okay, you're cheating: It's {cheat}")  
            return 1000
        else:
            print("You entered the wrong input, try again")
            continue


def check_guess(guess, computer_number):
    """Check the guesses number against the predefined random number"""
    if guess == computer_number:
        return True
    elif guess < computer_number:
        clear_screen()
        print("Too low!")
        return False
    else:
        clear_screen()
        print("Too High!")
        return False


def next_round():
    """Ask the player, if a next round is desired"""
    while True:
        new_game = str(input("Do you want to play another round? " +
                             "Type 'yes' or 'no': \n")).lower()
        if new_game == "yes":
            clear_screen()
            return True
        elif new_game == "no":
            return False
        else:
            "You entered the wrong input, try again"
            continue

# -------------------------Notes-----------------------------------------------*\
#
# -----------------------------------------------------------------------------*\
