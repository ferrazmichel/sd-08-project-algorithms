def is_palindrome_recursive(word, low_index, high_index):
    if not word:
        return False
    if word[low_index] == word[high_index]:
        if low_index == high_index or low_index == high_index - 1:
            return True
        else:
            return is_palindrome_recursive(word, low_index + 1, high_index - 1)
    else:
        return False

