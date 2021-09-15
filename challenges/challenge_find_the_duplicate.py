from typing import Counter


def find_duplicate(nums):
    """ Faça o código aqui. """
    if len(nums) <= 1 or any(type(num) != int or num < 0 for num in nums):
        return False

    DUPLICATE_DICT = Counter(nums)
    if all(value == 1 for value in DUPLICATE_DICT.values()):
        return False

    return max(DUPLICATE_DICT, key=DUPLICATE_DICT.get)
