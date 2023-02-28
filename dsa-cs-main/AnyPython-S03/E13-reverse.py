"""
File: reverse.py
----------------
This program shows an example of reversing a string, character by character.
"""


def reverse(str):
    """
    Takes a string and returns a reversed copy
    >>> reverse('stressed')
    'desserts'
    >>> reverse('hello')
    'olleh'
    """
    result = ''
    for i in range(len(str)-1, -1, -1): # counts from len(str)-1 down to 0 (including 0)
        ch = str[i]
        result += ch
    return result


def reverse2(str):
    """
    Complete a function, reverse2(), using string concatenation
    """
    pass


def reverse3(str):
    """
    This uses the slice operator with no start, no end, and a step of -1,
    so slice reverses.
    """
    pass


def main():
    x = input('Enter a string: ')
    rev = reverse(x)
    print(x + ' spelled backwards is ' + rev)


if __name__ == '__main__':
    main()

