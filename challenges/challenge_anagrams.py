def merge_sort(string_list):
    if len(string_list) <= 1:
        return string_list

    middle_index = len(string_list) // 2

    left_part, right_part = merge_sort(string_list[:middle_index]), merge_sort(
        string_list[middle_index:]
    )

    return merge(left_part, right_part, string_list.copy())


def merge(left_part, right_part, merged):
    left_index, right_index = 0, 0

    while left_index < len(left_part) and right_index < len(right_part):
        if left_part[left_index] <= right_part[right_index]:
            merged[left_index + right_index] = left_part[left_index]
            left_index += 1
        else:
            merged[left_index + right_index] = right_part[right_index]
            right_index += 1

    for left_index in range(left_index, len(left_part)):
        merged[left_index + right_index] = left_part[left_index]

    for right_index in range(right_index, len(right_part)):
        merged[left_index + right_index] = right_part[right_index]

    return merged


def is_anagram(first_string, second_string):
    """Faça o código aqui."""
    if len(first_string) != len(second_string) or len(first_string) == 0:
        return False

    first_string_list = merge_sort(list(first_string))
    second_string_list = merge_sort(list(second_string))

    for index in range(0, len(first_string_list)):
        if first_string_list[index] != second_string_list[index]:
            return False

    return True
