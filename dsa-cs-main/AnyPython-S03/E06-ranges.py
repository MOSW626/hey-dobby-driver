"""
File: ranges.py
-------------------
Practice range() function
"""


def main():
    # Type command on Terminal or Run this
    # range(n) - 1 Parameter Form
    s = 'Python'
    len(s)
    for i in range(len(s)):
        print(i, s[i])
    list(range(5))
    list(range(10))
    list(range(2))
    list(range(1))
    list(range(0))  # n <= 0, no numbers
    list(range(-42))

    # reversed() Variation
    s = 'Python'
    len(s)
    for i in reversed(range(len(s))):
        print(i, s[i])

    # range(start, stop) - 2 Parameter Form
    list(range(5, 10))
    list(range(5, 7))
    list(range(5, 6))
    list(range(5, 5))  # start >= stop, no numbers
    list(range(0, 5))
    list(range(0, 0))
    list(range(0, -1))

    # range(start, stop, step) - 3 Parameter Form
    list(range(0, 10, 2))
    list(range(0, 10, 6))
    list(range(200, 800, 100))
    list(range(10, 5, -1))
    list(range(10, 5, -2))
    list(range(6, 5, -2))
    list(range(5, 5, -2))  # equal to stop is omitted
    list(range(4, 5, -2))  # beyond the stop is omitted

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()