# solução parcial em:
# https://www.geeksforgeeks.org/python-program-check-string-palindrome-not/
def is_palindrome_iterative(word):
    """ Faça o código aqui. """
    if not word:
        return False
    return word == word[::-1]
