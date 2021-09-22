def is_anagram(first_string, second_string):

    if not first_string or not second_string:
        return False

    first_array = list(first_string)
    second_array = list(second_string)

    for index in first_array:
        if index in second_array:
            second_array.remove(index)
        else:
            return False

    if len(second_array) != 0:
        return False
    else:
        return True
