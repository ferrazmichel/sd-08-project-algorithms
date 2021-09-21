def is_anagram(first_string, second_string):
    if not first_string and not second_string:
        return False

    f_string = insertion_sort(first_string)
    s_string = insertion_sort(second_string)

    if f_string == s_string:
        return True
    else:
        return False


def insertion_sort(string):
    array = list(string)
    for i in range(len(array)):
        current_value = array[i]
        current_position = i
        while (
            current_position > 0
            and array[current_position - 1] > current_value
        ):
            array[current_position] = array[current_position - 1]
            current_position = current_position - 1
        array[current_position] = current_value
    return ''.join(array)
