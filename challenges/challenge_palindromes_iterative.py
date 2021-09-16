# https://www.geeksforgeeks.org/python-program-check-string-palindrome-not/
def is_palindrome_iterative(word):
    if not word:
        return False

    return word == word[::-1]
