def is_palindrome_iterative(word):
    '''
    Receives a string, start index and end index

    Returns True if the string is a palindrome and False if
    it is empty or not a palindrome.
    '''
    if not word:
        return False
    low_index = 0
    high_index = len(word) - 1

    while low_index < high_index:
        if word[low_index] != word[high_index]:
            return False
        low_index += 1
        high_index -= 1
    return True
