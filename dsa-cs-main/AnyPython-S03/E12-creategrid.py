"""
File: creategrid.py
-----------------
This program create 2-D lists, i.e., grid by giving
# of rows and # of columns.
"""


def create_grid(rows, cols, value):
    """
    This function create rows by cols 2-D lists. Then,
    return a grid.
    """
    grid = []
    """
    Add your code here.
    """
    return grid


def main():
    rows = int(input("How many rows? "))
    cols = int(input("How many columns? "))
    val = int(input("What is a default value? "))
    my_list = create_grid(rows, cols, val)
    print(my_list)


if __name__ == '__main__':
    main()