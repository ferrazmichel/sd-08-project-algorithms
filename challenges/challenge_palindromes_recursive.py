# def recursive_palindrome(word):
#     if len(word) == 0:
#         return False
#     if len(word) < 2:
#         return word
#     else:
#         return recursive_palindrome(word[1:]) + word[0]


def is_palindrome_recursive(word, low_index, high_index):
    if len(word) == 0:
        return False

    # caso a palavra na mesma posição oposta for diferente retorna False
    if word[high_index] != word[low_index]:
        return False

    """quando os index tanto o low quanto o high chegarem ao meio
    (quando for ímpar) ou o low for maior que o high (quando for par)
    significa que é palíndromo pois percorreram a primeira e a segunda
    metade comparando os caracteres opostos"""
    if high_index == low_index or low_index > high_index:
        return True

    # vai chamando a função e aumentando low e diminuindo o high
    return is_palindrome_recursive(word, low_index + 1, high_index - 1)
