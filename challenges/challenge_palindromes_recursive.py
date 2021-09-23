def is_palindrome_recursive(word, low_index, high_index):
    '''
    Receives a string, start index and end index

    Returns True if the string is a palindrome and False if
    it is empty or not a palindrome.
    '''
    if not word or word[low_index] != word[high_index]:
        return False
    elif low_index >= high_index:
        return True

    return is_palindrome_recursive(word, low_index + 1, high_index - 1)
