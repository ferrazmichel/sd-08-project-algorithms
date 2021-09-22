def is_palindrome_recursive(word, low_index, high_index):
    """ Faça o código aqui.
    https://stackoverflow.com/questions/30340208/recursively-checking-if-a-list-is-a-palindrome-in-python
    """
    if not word:
        return False

    if low_index == high_index or high_index < low_index:
        return True

    return (word[low_index] == word[high_index]
            and is_palindrome_recursive(word, low_index + 1, high_index - 1))
