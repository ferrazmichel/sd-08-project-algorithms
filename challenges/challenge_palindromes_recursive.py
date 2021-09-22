def is_palindrome_recursive(word, low_index, high_index):
    """ Given a string, returns true if its a palindrome """
    if len(word) == 0 or word[low_index] != word[high_index]:
        return False
    if len(word) < 2:
        return True
    return is_palindrome_recursive(word[1:high_index], low_index, -1)
