def is_palindrome_iterative(word):
    """ Faça o código aqui. """
    if not word:
        return False
    if len(word) == 1:
        return True
    reversed_word = ""
    for i in range(len(word)-1, -1, -1):
        reversed_word += word[i]
    return word == reversed_word
