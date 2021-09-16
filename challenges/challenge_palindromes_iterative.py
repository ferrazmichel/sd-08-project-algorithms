
def is_palindrome_iterative(word):
    if not word:
        return False
    drow = word[::-1]
    if drow == word:
        return True
    return False
