"""
File: asktokarel.py
------------------
Ask a yes or no questions. Then, answer randomly
"""
import random

def main():
    # Good practice to save any input as a variable
    question = input("Ask a yes or no question to Karel: ")
    choice = random.randint(1, 6)
    # 1: No chance
    # 2: Without a doubt
    # 3: The answer can be found in the tea room
    # 4: Yes!
    # 5: Good question
    # 6: Only Karel knows

    print('')


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()