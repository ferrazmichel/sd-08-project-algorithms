def is_anagram(first_string, second_string):
    if not first_string or not second_string:
        return False

    while first_string:
        character = first_string[0]
        first_arr = first_string.split(character)
        second_arr = second_string.split(character)
        if len(first_arr) != len(second_arr):
            return False
        first_string = "".join(first_arr)
        second_string = "".join(second_arr)
    return True
