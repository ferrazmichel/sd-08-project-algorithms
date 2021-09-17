def is_palindrome_recursive(word, low_index, high_index):
    if len(word) == 0 or high_index < low_index:
        return False
    if high_index == low_index:
        return True
    if word[high_index] != word[low_index]:
        return False

    return is_palindrome_recursive(word, low_index + 1, high_index - 1)
