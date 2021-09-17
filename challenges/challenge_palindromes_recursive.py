def reverse_word(word, low_index, high_index):
    length_word = len(word[low_index:high_index])

    if length_word < 2:
        return word
    else:
        return reverse_word(word[1:], low_index, high_index) + word[0]


def is_palindrome_recursive(word, low_index, high_index):
    """ Faça o código aqui. """

    if not word:
        return False

    return reverse_word(word, low_index, high_index) == word
