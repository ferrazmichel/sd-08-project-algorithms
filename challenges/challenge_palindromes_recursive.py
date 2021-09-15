def reverse(list):
    if len(list) < 2:
        return list
    else:
        return reverse(list[1:]) + [list[0]]


def is_palindrome_recursive(word, low_index, high_index):
    """Faça o código aqui."""
    if not isinstance(word, str) or len(word) == 0:
        return False
    reverse_word_list = reverse(list(word))
    reverse_word = "".join(reverse_word_list)
    if reverse_word != word:
        return False

    return True
