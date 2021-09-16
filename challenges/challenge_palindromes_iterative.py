def is_palindrome_iterative(word):
    """ Faça o código aqui. """
    if not word:
        return False
    if word[::-1] == word:
        return True
    if word[::-1] != word:
        return False
