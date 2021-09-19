def bubble_sort(array):
    has_swapped = True
    num_of_iterations = 0
    while has_swapped:
        has_swapped = False
        for i in range(len(array) - num_of_iterations - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                has_swapped = True
        num_of_iterations += 1
    return array


def is_anagram(first_string, second_string):
    first = bubble_sort(first_string.split())
    second = bubble_sort(second_string.split())
    return "".join(first) == "".join(second)
