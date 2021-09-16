def is_anagram(first_string, second_string):
    if not first_string or not second_string:
        return False
    return sorted(first_string.lower()) == sorted(second_string.lower())
