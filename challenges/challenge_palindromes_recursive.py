def is_palindrome_recursive(word, low_index, high_index):
    """ Faça o código aqui. """
    if low_index < high_index and len(word) > 0:
        if word[low_index] == word[high_index]:
            return is_palindrome_recursive(word, low_index + 1, high_index - 1)
        else:
            return False
    elif low_index >= high_index and high_index > 0:
        print(low_index, high_index)
        return True
    else:
        return False
