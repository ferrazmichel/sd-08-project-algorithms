def is_palindrome_iterative(word):
    """ Faça o código aqui. """
    # https://www.w3schools.com/python/python_howto_reverse_string.asp
    if word == '':
        return False

    return word == word[::-1]
