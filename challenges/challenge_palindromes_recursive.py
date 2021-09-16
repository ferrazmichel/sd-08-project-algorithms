def is_palindrome_recursive(word, low_index, high_index):
    """ Faça o código aqui. """
    try:
        if word == "" or word[low_index] != word[high_index]:
            return False
        elif low_index == high_index:
            return True
        else:
            return (
                is_palindrome_recursive(
                    word,
                    low_index + 1,
                    high_index - 1)
            )
    except IndexError:
        return False

# References
# https://www.geeksforgeeks.org/recursive-function-check-string-palindrome/
# https://stackoverflow.com/questions/952110/recursive-function-palindrome-in-python
# From a general algorithm perspective, the recursive function has 3 cases:
# 1) 0 items left. Item is a palindrome, by identity.
# 2) 1 item left. Item is a palindrome, by identity.
# 3) 2 or more items. Remove first and last
#  item. Compare. If they are the same,
# call function on what's left of string. If first and last are not the same,
# item is not a palindrome.
# The implementation of the function itself
# is left as an exercise to the reader :)
# PYTHON Recursion - Palindrome recursive function:
# https://www.youtube.com/watch?v=92UyahoAne4
