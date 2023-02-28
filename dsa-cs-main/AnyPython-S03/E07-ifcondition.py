"""
File: ifcondition.py
------------------
Ask the user for numbers. Then, print 0 or "Positive" or
"Negative".
"""

def main():
    num = int(input("Enter a number: "))
    if num == 0:
        print("Your number is 0 ")
    # Make it better!!


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()