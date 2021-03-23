""" module with square_preceding function """
from typing import List


def square_preceding(values: List[int or float]):
    """
    Replace each item in the list with square the value of the
    preceding item, and replace the first item with 0.
    >>> lst = [1, 2, 3.]
    >>> square_preceding(lst)
    >>> lst
    [0, 1, 4]
    >>> lst = []
    >>> square_preceding(lst)
    >>> lst
    []
    """
    if values:
        temp = values[0]
        for i in range(1, len(values)):
            temp0 = values[i]
            values[i] = temp ** 2
            temp = temp0
        values[0] = 0
