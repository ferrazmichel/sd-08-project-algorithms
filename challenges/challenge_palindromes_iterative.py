def is_palindrome_iterative(word):
    """ Faça o código aqui. """
    size = len(word)
    if size < 1:
        return False
    for index in range(size // 2):
        if word[index] != word[size - index - 1]:
            return False
    return True
