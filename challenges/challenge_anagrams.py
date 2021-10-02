def ordenar_string(array):
    """Função para ordenar a string."""
    # Função de ordenação retirada do course que utiliza a tecnica merge sort
    if len(array) <= 1:
        return array

    metade = len(array) // 2

    left, right = ordenar_string(array[:metade]), ordenar_string(array[metade:])
    return merge(left, right, array.copy())


def merge(left, right, merged):
    """Função para mergear."""
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


def is_anagram(first_string, second_string):
    """Função para descobir anagramas""" 
    if len(first_string) != len(second_string):
        return False

    if ordenar_string(list(first_string)) == ordenar_string(list(second_string)):
        return True
    else:
        return False
