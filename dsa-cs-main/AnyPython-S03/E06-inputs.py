"""
File: inputs.py
-------------------
Practice input() function
"""


def main():
    # Type command on Terminal or Run this
    # Input
    name = input('what is your name? ')
    print(name)

    # String Conversion
    #age = input('what is your age? ')
    #print(type(age))
    #print(type(int(age)))

    # Input In A Function
    #your_age = get_age()
    #print(your_age)


def get_age():
    """
    Prompt the user for their int age and
    return it as an int.
    """
    pass
    #age_str from 'What is your age in years? '

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()