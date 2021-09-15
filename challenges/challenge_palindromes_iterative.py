def is_palindrome_iterative(word):
    """ Faça o código aqui. """
    if len(word) <= 1:
        return False

    for index in range(len(word)):
        if word[index] != word[-index - 1]:
            return False

    return True
