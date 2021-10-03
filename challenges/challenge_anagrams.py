def merge(left, right):
    new_string = ""
    left_cursor, right_cursor = 0, 0

    while left_cursor < len(left) and right_cursor < len(right):

        if left[left_cursor] <= right[right_cursor]:
            new_string += left[left_cursor]
            left_cursor += 1
        else:
            new_string += right[right_cursor]
            right_cursor += 1
    for left_cursor in range(left_cursor, len(left)):
        new_string += left[left_cursor]
    for right_cursor in range(right_cursor, len(right)):
        new_string += right[right_cursor]

    return new_string


def merge_sort(string):
    if len(string) <= 1:
        return string
    mid = len(string) // 2
    left, right = merge_sort(string[:mid]), merge_sort(string[mid:])
    return merge(left, right)


def is_anagram(first_string, second_string):
    first = merge_sort(first_string)
    second = merge_sort(second_string)
    return first == second
