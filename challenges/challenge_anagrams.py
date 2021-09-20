# solução em:
# https://www.geeksforgeeks.org/python-sorted-check-two-strings-anagram-not/
from collections import Counter


def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    if Counter(first_string) == Counter(second_string):
        return True
    else:
        return False
