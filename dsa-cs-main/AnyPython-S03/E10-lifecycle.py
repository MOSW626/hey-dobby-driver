"""
File: lifecycle.py
----------------------
Example program to show scope of variables for each
namespaces, i.e., Built-in, Global, Enclosed, and Local.
Please, modify local_function() to display global variable
(i.e., "global").
"""

# Global variable – visible to all functions
x = 'global'


def main():
    x = 'main'
    local_funtion()
    print(x)


def local_funtion():
    x = 'local'
    print(x)


if __name__ == '__main__':
    main()
