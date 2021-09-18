def is_anagram(first_string, second_string):
    first_string_array = list(first_string)
    second_string_array = list(second_string)

    for char in first_string_array:
        if char in second_string_array:
            second_string_array.remove(char)
        else:
            return False
    return len(second_string_array) == 0
