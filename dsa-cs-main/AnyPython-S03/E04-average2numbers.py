"""
File: average2numbers.py
------------------------
This program asks the user for two numbers
and prints their average.
"""

def main():
    print("This program averages two numbers.")
    first_num = float(input("Enter first number: "))
    second_num = float(input("Enter second number: "))
    total = first_num + second_num / 2     # buggy! Fix the problem
    print("The average is", total)


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
