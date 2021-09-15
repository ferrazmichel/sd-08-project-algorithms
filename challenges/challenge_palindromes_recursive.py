def is_palindrome_recursive(word, low_index, high_index):
    """ Faça o código aqui. """

    if word == "":
        return False
    if high_index == 0:
        return True

    if low_index == high_index:
        return True
    if (word[low_index] == word[high_index]):
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
    return False
