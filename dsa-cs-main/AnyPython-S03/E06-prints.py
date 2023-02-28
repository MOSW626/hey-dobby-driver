"""
File: prints.py
-------------------
Practice print() function
"""


def main():
    # Type command on Terminal or Run this
    # print : HelloWorld
    print("Hello World!")

    # print function
    print(12, 24, -2)
    print('hi', 'there', -2)
    print('woot')  # 1 item, 1 \n
    print()  # 0 items, 1 \n
    print('Hello')

    # Print Option sep=
    print(12, 24, -2, sep=':')
    print('but', 'not', 'including', sep='**')
    print('but', 'not', 'including', sep='')  # empty string

    # Print Option end=
    print('hello\n')
    print('there\n')
    print('hello\n', end='')
    print('there\n', end='')

    # Print To File
    filename = "print.txt"
    with open(filename, 'w') as f:
        print('Hello world', file=f)

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()