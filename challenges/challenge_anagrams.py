def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    if first_string == "" or second_string == "":
        return False
    lista = list(first_string)
    lista1 = list(first_string)
    if len(lista) != len(lista1):
        return False

    order_list(lista)
    order_list(lista1)
    # o "if" testa se a string acessada pelo índice (j + 1)
    # precede a string acessada pelo índice "j"
    # k = 0
    # if lista1[k] > lista1[k + 1]:
    #     # faz a troca dos elementos
    #     aux1 = lista1[k]
    #     lista1[k] = lista1[k + 1]
    #     lista1[k + 1] = aux1
    #     k += 1

    if lista == lista1:
        return True

    # if lista != lista1:
    #     return False
    return is_anagram(first_string, second_string)


def order_list(word_list):
    j = 0
    if word_list[j] > word_list[j + 1]:
        # o "if" testa se a string acessada pelo índice (j + 1)
        # precede a string acessada pelo índice "j"
        # faz a troca dos elementos
        aux = word_list[j]
        word_list[j] = word_list[j + 1]
        word_list[j + 1] = aux
        j += 1
    return word_list
