def is_palindrome_iterative(word):
    """Função iterativa para verificar se uma palavra é palindrome."""
    if word == '':
        return False

    for posicao in range(len(word) // 2):
        if word[posicao] != word[-1]:
            return False
        else:
            word = word[:len(word) - 1]

    return True
