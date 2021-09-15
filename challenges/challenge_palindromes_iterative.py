def is_palindrome_iterative(word):
    """Faça o código aqui."""
    if not isinstance(word, str) or len(word) == 0:
        return False
    reverse_word = word[::-1]
    if reverse_word != word:
        return False

    return True
