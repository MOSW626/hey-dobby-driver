"""
File: spread.py
---------------
This program simulates the spread of an infection in a population.  A world
is represented as a list of lists (2-dimensional list), where each cell
contains either a person who is negative for a condition ('-'), a person who
is positive for a condition ('+'), no person but the cell is within reach of
infection ('.'), or is empty and not within reach of infection(None).
An initial infection point is specified and all people within RADIUS cells
around that point (i.e., a square) are infected.  Iteratively, all newly
infected people can infect others who are within RADIUS cells of them.  The
simulation continues until no new infections are detected.
"""

import random


SIZE = 10       # The world used will be SIZE x SIZE
RADIUS = 1      # Radius around which an infection spreads
DENSITY = 0.25  # Probability that a cell starts with a (negative) person in it


def initialize_grid(n):
    """
    Creates and returns a grid (list of lists), that has n rows and
    each row has n columns.  All the elements in the grid are set to
    random values, representing None (no one) or '-' (person who is
    negative for the initial condition) based on DENSITY of people.
    """
    grid = []                           # Create empty grid
    for row in range(n):                # Create rows one at a time
        row = []
        for col in range(n):            # Build up each row by appending to a list
            chance = random.random()    # Get random float between 0.0 and 1.0
            if chance < DENSITY:        # Add a person (who is negative)
                row.append('-')
            else:
                row.append(None)        # Add an "empty" cell
        grid.append(row)                # Append the row (list) onto grid

    return grid


def set_infection(grid, row, col):
    """
    Given a grid and an infection point (col, row), this function sets any person
    who is negative within RADIUS squares of the infection point to be positive
    (denoted by '+') and any other cells to '.' to denoted they were exposed.
    The function returns True if any previously negative people were infected
    (i.e., become positive), False otherwise.
    """
    start_row = row - RADIUS
    end_row = row + RADIUS
    start_col = col - RADIUS
    end_col = col + RADIUS
    infected = False

    for row in range(start_row, end_row + 1):
        for col in range(start_col, end_col + 1):
            if row >= 0 and row < SIZE and col >= 0 and col < SIZE:
                if grid[row][col] == '-':   # negative people become positive
                    grid[row][col] = '+'
                    infected = True
                elif not grid[row][col]:    # "not grid[row][col]" checks for None
                    grid[row][col] = '.'    # empty cells marked as infected

    return infected


def spread_infection(grid):
    """
    Loops through all cells in the grid and for every positive person,
    it makes them an infection point to potentially spread infection.
    The function returns True if any previously negative people were infected
    (i.e., become positive), False otherwise.
    """
    infected = False
    rows = len(grid)                    # Could have used SIZE, but wanted
    cols = len(grid[0])                 # to show a different way to do this.

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == '+':   # Positive person is an infection point
                new_infection = set_infection(grid, row, col)
                infected = infected or new_infection

    return infected


def get_value_in_range(prompt, min, max):
    """
    Asks the user for a value using the prompt string.  Checks if
    user entered value is between min and max (inclusive) and prompts
    the user if the value is out of range.  Returns a valid value entered
    by the user.
    """
    while True:
        value = int(input(prompt))
        if value >= min and value <= max:
            return value
        print("Invalid entry.  Please enter a value between", min, "and", max)


def print_borderline(length):
    """
    Prints a border line of (length + 1) #'s, with leading spaces
    """
    print('  ', end='')
    for i in range(length + 1):
        print('# ', end='')
    print('#')


def print_column_indexes(length):
    """
    Prints the column index numbers (length of them), appropriately spaced
    """
    print('    ', end='')
    for i in range(length):
        print_formatted(i)
    print('')       # Print a "return" to end the line


def print_formatted(num):
    """
    Prints a one or two digit number in two spaces
    """
    if num < 10:
        print(str(num) + ' ', end='')
    else:
        print(str(num), end='')


def print_grid(grid):
    """
    Prints out grid, including row/column index numbers and borders
    """
    print_column_indexes(SIZE)
    print_borderline(SIZE)

    rows = len(grid)                    # Could have used SIZE, but wanted
    cols = len(grid[0])                 # to show a different way to do this.
    for row in range(rows):
        print_formatted(row)
        print('# ', end='')             # Print left-hand border
        for col in range(cols):
            symbol = grid[row][col]
            if not symbol:              # Print a space if symbol is None
                print(' ', end='')
            else:
                print(symbol, end='')
            print(' ', end='')          # Prints space for paddingS
        print('#')                      # Print right-hand border (and return)
    print_borderline(SIZE)


def main():
    """
    Create the initial (random) grid, ask the user for an initial infection
    point and then keep spreading the infection until no new people in the
    simulation are infected.  Print out the initial and final grids
    """
    random.seed(2)
    pass


if __name__ == '__main__':
    main()
