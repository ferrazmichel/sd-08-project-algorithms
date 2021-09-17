def is_palindrome_recursive(word, low_index, high_index):
# referencia https://www.delftstack.com/pt/howto/python/python-palindrome/
    if word == '' and word[low_index] != word[high_index]:
        return False
    if word == "".join(reversed(word)):
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
    return True
