def is_palindrome_recursive(word, low_index, high_index):
    """ Faça o código aqui. """
    if len(word) == 0:
        return False
    if low_index == high_index:
        return True
    if word[low_index] != word[high_index]:
        return False
    if low_index < high_index + 1:
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)


# Solução encontrada no link:
# https://www.geeksforgeeks.org/recursive-function-check-string-palindrome/
# Se houver um único caractere ele retorna True, por isso a comparação entre 
# low e high;
# Se a palava no index low for diferente no index high retorna False, pois 
# eles não correspondem;
# Se index low for menor que o high ele faz a recursividade aumentado o low
# e diminuindo o high.
