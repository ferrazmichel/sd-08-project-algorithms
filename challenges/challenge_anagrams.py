from collections import Counter


def is_anagram(first_string, second_string):
    if not bool(first_string) or not bool(
      second_string) or len(first_string) != len(second_string):
        return False
    return Counter(first_string) == Counter(second_string)
