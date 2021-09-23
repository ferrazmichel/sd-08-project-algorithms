def is_palindrome_recursive(word, low_index, high_index):
    list_word = list(word)

    if len(word) < 1:
        return False
    if low_index == high_index:
        return True
    if list_word[high_index] != list_word[low_index]:
        return False
    return is_palindrome_recursive(list_word, low_index + 1, high_index - 1)
