def is_anagram(first_string, second_string):
    reverse = "".join(list(second_string)[::-1])
    if len(first_string) != len(second_string):
        return False
