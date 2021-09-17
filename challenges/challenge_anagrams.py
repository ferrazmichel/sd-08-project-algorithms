def is_anagram(first_string, second_string):
    """ 3.1 - Retorne true se as palavras passadas forem anagramas; 3.2 -
    Retorne false se as palavras passadas por parâmetro não forem anagramas;
    3.3 - Retorne false se alguma das palavras passadas por parâmetro for uma
    string vazia; 3.4 - Execute a função, somando 10.000 execuções para uma
    entrada pequena, em menos que 8.2s (tempo da execução do avaliador no Pull
    Request)"""

    return merge_sort([letter for letter in first_string]) == merge_sort(
        [letter for letter in second_string]
    )


def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2

    left, right = merge_sort(array[:mid]), merge_sort(array[mid:])

    return merge(left, right, array.copy())


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
