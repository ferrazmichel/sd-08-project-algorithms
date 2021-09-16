def is_palindrome_iterative(word):
    """ Faça o código aqui. """

    # https://stackoverflow.com/questions/9027862/what-does-listxy-do

    return word != "" and word == word[::-1]
