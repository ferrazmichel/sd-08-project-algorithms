# Reversing string in python:
# https://www.w3schools.com/python/python_howto_reverse_string.asp
def is_palindrome_iterative(word):
    if word == "" or word != word[::-1]:
        return False
    return True
