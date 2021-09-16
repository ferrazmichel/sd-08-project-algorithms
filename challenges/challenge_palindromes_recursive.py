def recursive_palindrome(word):
    if len(word) == 0:
        return False
    if len(word) < 2:
        return word
    else:
        return recursive_palindrome(word[1:]) + word[0]


def is_palindrome_recursive(word):
    reversed_word = recursive_palindrome(word)
    if(reversed_word == word):
        return True
    return False


