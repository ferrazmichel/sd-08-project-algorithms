def is_palindrome_iterative(word):
    """ Faça o código aqui. """
    if len(word) <= 1:
        return False

    return word == word[::-1]
