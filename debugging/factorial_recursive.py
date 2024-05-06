#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function description:
    Calculates the factorial of a given integer.

    Parameters:
    - n: An integer for which factorial needs to be calculated.

    Returns:
    An integer representing the factorial of the input number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)
