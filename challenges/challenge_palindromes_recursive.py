def is_palindrome_recursive(word, low_index, high_index):
    """ Faça o código aqui. """
    if word == '':
        return False

    if len(word) > 1:
        if word[0] != word[-1]:
            return False

        else:
            is_palindrome_recursive(word[1:high_index], 0, high_index - 1)

    else:
        return True
