def is_palindrome_iterative(word):
    """ Faça o código aqui. """
    if word == '':
        return False
    inverted_word = word[::-1]
    return inverted_word == word
