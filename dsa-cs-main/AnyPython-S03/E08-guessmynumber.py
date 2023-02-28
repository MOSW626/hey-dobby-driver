"""
File: guessmynumber.py
----------------------
Computer is thinking one number 1 ~ 99
You are guessing the number until correct
"""

import random

def main():
    secret_number = random.randint(1, 99)
    print("I am thinking of a number between 1 and 99...")

    # True if guess is not equal to secret number
    while ???:
        # Get a new guess


        # True if guess is less than secret number


    print("Congrats! The number was: " + str(secret_number))

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()