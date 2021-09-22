def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2

    left, right = merge_sort(array[:mid]), merge_sort(array[mid:])

    return merge(left, right)


def merge(left_array, right_array):
    left_index = right_index = 0
    left_length, right_length = len(left_array), len(right_array)

    merged = []

    while (left_index < left_length) and (right_index < right_length):
        if left_array[left_index] <= right_array[right_index]:
            merged.append(left_array[left_index])
            left_index += 1
        else:
            merged.append(right_array[right_index])
            right_index += 1

    return merged + left_array[left_index:] + right_array[right_index:]
