def is_palidrome_even(word, low_index, high_index):
    if low_index == high_index - 1 and word[low_index] == word[high_index]:
        return True
    elif word[low_index] == word[high_index]:
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
    else:
        return False


def is_palidrome_odd(word, low_index, high_index):
    if low_index == high_index:
        return True
    elif word[low_index] == word[high_index]:
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
    else:
        return False


def is_palindrome_recursive(word, low_index, high_index):
    """ Faça o código aqui. """
    if not word:
        return False
    elif len(word) % 2 == 0:
        return is_palidrome_even(word, low_index, high_index)
    else:
        return is_palidrome_odd(word, low_index, high_index)
