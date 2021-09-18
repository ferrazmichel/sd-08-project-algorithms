def merge(left, right, merged):
    left_cursor, right_cursor = 0, 0
    while left_cursor < len(left) and right_cursor < len(right):
        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor + right_cursor] = left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1
    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]
    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]
    return merged


# Trybe - Bloco 36 -  Algoritmos
def mergesort(array):   # complexidade de O(n log n)
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left, right = mergesort(array[:mid]), mergesort(array[mid:])
    return merge(left, right, array.copy())


def is_anagram(first_string, second_string):
    if not first_string or not second_string:
        return False
    if len(first_string) != len(second_string):
        return False
    return mergesort(list(first_string)) == mergesort(list(second_string))
