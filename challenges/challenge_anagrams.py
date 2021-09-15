def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    if ((first_string is None) or first_string == ''):
        return False
    if ((second_string is None) or second_string == ''):
        return False
    first_string_sorted = ''.join(
        quick_sort(list(first_string), 0, len(first_string) - 1)
        )
    second_string_sorted = ''.join(
        quick_sort(list(second_string), 0, len(second_string) - 1)
        )
    if (first_string_sorted == second_string_sorted):
        return True
    else:
        return False


def shifts(char_list, pivot, pivot_position, start_index, end_index):
    rightShift = False
    leftShift = False

    # RightShift
    min_for_right_shift = min(char_list[pivot_position:end_index + 1])
    min_position = char_list.index(min_for_right_shift)
    if (pivot > min_for_right_shift):
        rightShift = True
        char_list[pivot_position] = min_for_right_shift
        char_list[min_position] = pivot
        pivot_position = min_position
        pivot = char_list[pivot_position]

    # LeftShit
    if (pivot_position != 0):
        max_for_left_shift = max(char_list[start_index:pivot_position])
        max_position = char_list.index(max_for_left_shift)
        if (pivot < max_for_left_shift):
            leftShift = True
            char_list[pivot_position] = max_for_left_shift
            char_list[max_position] = pivot
            pivot_position = max_position
            pivot = char_list[pivot_position]

    return [leftShift, rightShift, pivot, pivot_position]


def quick_sort(char_list, start_index, end_index):
    starting_pivot = char_list[start_index]

    pivot_position = start_index
    pivot = char_list[pivot_position]

    rightShift = True
    leftShift = True

    while (rightShift and leftShift):
        rightShift = False
        leftShift = False

        rightShift, leftShift, pivot, pivot_position = shifts(
            char_list, pivot, pivot_position, start_index, end_index
            )

    if(end_index - start_index == 1):
        return char_list
    if(char_list[start_index] == starting_pivot):
        return quick_sort(char_list, start_index + 1, end_index)
    if(char_list[end_index] == starting_pivot):
        return quick_sort(char_list, start_index, end_index - 1)
    return char_list
