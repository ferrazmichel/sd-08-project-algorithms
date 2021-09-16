def quicksort(array, low, high):
    """Quicksort - tal como implementado no course"""
    if len(array) == 1:
        return array
    if low < high:
        partition_index = partition(array, low, high)
        quicksort(array, low, partition_index - 1)
        quicksort(array, partition_index + 1, high)


def partition(array, low, high):
    """Função auxiliar para o quicksort"""
    i = low - 1
    pivot = array[high]
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]

    return i + 1


def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    if not first_string or not second_string:
        return False
    first_string_list = list(first_string)
    second_string_list = list(second_string)
    quicksort(first_string_list, 0, len(first_string_list) - 1)
    quicksort(second_string_list, 0, len(second_string_list) - 1)
    return first_string_list == second_string_list
