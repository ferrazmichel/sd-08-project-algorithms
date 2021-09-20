# Solução em:
# https://www.geeksforgeeks.org/recursive-function-check-string-palindrome/
def is_palindrome_recursive(word, low_index, high_index):
    """ Faça o código aqui. """
    if not word:
        return False

    if low_index == high_index:
        return True

    if word[low_index] != word[high_index]:
        return False

    if low_index < high_index + 1:
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)

    return True
