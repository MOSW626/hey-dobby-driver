"""
File: globals.py
----------------------
Example program to show why global variables are bad style.
"""

# Constant – visible to all functions
NUM_DAYS_IN_WEEK = 7

# Global variable – visible to all functions
balance = 0


def main():
    balance = int(input("Initial balance: "))
    while True:
        amount = int(input("Deposit (0 to quit): "))
        if amount == 0:
            break
        deposit(amount)
    print("Total balance is ", balance)

def deposit(amount):
    balance += amount


if __name__ == '__main__':
    main()
