def is_palindrome_iterative(word):
    if not word:
        return False
    # https://www.w3schools.com/python/python_howto_reverse_string.asp
    return word == word[::-1]
