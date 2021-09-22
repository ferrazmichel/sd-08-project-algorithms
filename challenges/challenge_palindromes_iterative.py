def is_palindrome_iterative(word):
    if len(word) == 0:
        return False
    reverse_word = word[::-1]
    if word == reverse_word:
        return True
    else:
        return False
