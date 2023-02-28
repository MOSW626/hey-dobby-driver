"""
File: examplereturn.py
------------------
Convert feet and inches to meters using a function
Example of using function return
"""
import math

METERS_PER_FEET = 0.3
INCH_PER_FEET = 12

def main():
    feet = int(input('num feet? '))
    inches = int(input('num inches? '))
    meters = feet_to_meters(feet, inches)
    print('num meters', meters)


def feet_to_meters(num_feet, num_inches):
    print('converting...')

    # this calculates num meters just using the "feet" not the "inches"
    # Enter your code here for meters_in_feet
    #

    # this calculates num meters just using the "inches"
    # Enter your code here for meters_in_inch
    #

    # add them up for your final answer
    return meters_in_feet + meters_in_inch


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
