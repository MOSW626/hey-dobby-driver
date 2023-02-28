"""
File: phonebook.py
------------------
Program to show an example of using dictionaries to maintain
a phonebook.
"""


def read_phone_numbers():
    """
    Ask the user for names/numbers to story in a phonebook (dictionary).
    Returns the phonebook.
    """
    phonebook = {}                   # Create empty phonebook

    while True:
        pass

    return phonebook


def print_phonebook(phonebook):
    """
    Prints out all the names/numbers in the phonebook.
    """
    pass


def lookup_numbers(phonebook):
    """
    Allow the user to lookup phone numbers in the phonebook
    by looking up the number associated with a name.
    """
    while True:
        name = input("Enter name to lookup: ")
        pass


def main():
    phonebook = read_phone_numbers()
    print_phonebook(phonebook)
    lookup_numbers(phonebook)


# Python boilerplate.
if __name__ == '__main__':
    main()
