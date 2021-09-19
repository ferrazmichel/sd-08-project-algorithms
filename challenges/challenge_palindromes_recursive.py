def is_palindrome_recursive(word, low_index, high_index):
    if not word:
        return False
    return _is_palindrome(word, low_index, high_index)


def _is_palindrome(word, low_index, high_index):
    if high_index < low_index:
        return True
    if word[low_index] != word[high_index]:
        return False
    return _is_palindrome(word, low_index + 1, high_index - 1)
