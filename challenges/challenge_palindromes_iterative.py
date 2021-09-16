def is_palindrome_iterative(word):
    """ Faça o código aqui. """
    if len(word) == 0:
        return False

    if len(word) == 1:
        return True

    for index in range(len(word) // 2):
        if word[index] != word[-(index + 1)]:
            return False

    return True
