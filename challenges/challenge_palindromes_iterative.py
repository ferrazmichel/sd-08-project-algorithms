def is_palindrome_iterative(word):
    if word == '':
        return False
    elif str(word) == str(word)[::-1]:
        return True
    else:
        return False
