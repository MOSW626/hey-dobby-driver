"""
File: sentinelloop.py
------------------
Ask the user for numbers until they enter a sentinel value. Then,
print out the sum.
"""

SENTINEL = -1

def main():
    total = 0
    while num != SENTINEL:
        num = int(input("Enter a number: "))
        total += num
    print("total is " + str(total))

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()