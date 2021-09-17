def is_palindrome_recursive(word, low_index, high_index):
# referencia https://www.delftstack.com/pt/howto/python/python-palindrome/
    if word == "":
        return False
    if (word[low_index] != word[high_index]):
        return False
    if low_index == high_index:
        return True
    if low_index > high_index:
        return False
    if (word[low_index] == word[high_index]):
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)


# ABCBA
# is_palindrome_recursive("ABCCBA", 0, 5)
# A B C  C B A, 0, 5
# A B C  C B A, 1, 4
# A B C  C B A, 2, 3

