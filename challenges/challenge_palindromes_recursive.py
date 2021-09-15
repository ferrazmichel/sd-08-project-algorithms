def is_palindrome_recursive(word, low_index, high_index):
    """ Faça o código aqui. """
    if word == "":
        return False

    if len(word[low_index:high_index + 1]) == 1:
        return True

    if (
        len(word[low_index:high_index + 1]) == 2
        and word[low_index] == word[high_index]
    ):
        return True

    low_and_high_index_is_equal = word[low_index] == word[high_index]
    return low_and_high_index_is_equal and is_palindrome_recursive(
        word, low_index + 1, high_index - 1
    )
