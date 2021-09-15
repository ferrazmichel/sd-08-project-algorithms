def is_palindrome_recursive(word, low_index, high_index):
    """ Faça o código aqui. """
    if (word is None) or len(word) == 0:
        return False
    if (low_index == high_index):
        return True
    if (high_index - low_index == 1):
        return word[low_index] == word[high_index]
    else:
        if (word[low_index] == word[high_index]):
            return is_palindrome_recursive(word, low_index + 1, high_index - 1)
        return False
