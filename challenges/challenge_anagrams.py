def is_anagram(first_string, second_string):
    if sorted(first_string) == sorted(second_string):
        return True
    if not first_string or not second_string:
        return False
    else:
        return False
