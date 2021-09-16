def is_palindrome_recursive(word, low_index, high_index):
    """ Faça o código aqui. """
    if not word:
        return False
    if len(word) == 1:
        return True
    if (
        low_index == len(word) - 1
        and high_index == 0
        and word[low_index] == word[high_index]
    ):
        return True
    return word[low_index] == word[high_index] and is_palindrome_recursive(
        word, low_index + 1, high_index - 1
    )
