def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    if first_string == "" or second_string == "":
        return False
    lista = list(first_string)
    lista1 = list(first_string)
    if len(lista) != len(lista1):
        return False
    # loop mais externo começando de (len_lista - 1) até 1 com decremento -1
    # o "if" testa se a string acessada pelo índice (j + 1)
    # precede a string acessada pelo índice "j"
    j = 0
    if(lista[j] > lista[j + 1]):
        # faz a troca dos elementos
        aux = lista[j]
        lista[j] = lista[j + 1]
        lista[j + 1] = aux
        j += 1

        # loop mais externo começando de (len_lista1 - 1) até 1 com decremento -1
        # o "if" testa se a string acessada pelo índice (j + 1)
        # precede a string acessada pelo índice "j"
    k = 0
    if(lista1[k] > lista1[k + 1]):
        # faz a troca dos elementos
        aux1 = lista1[k]
        lista1[k] = lista1[k + 1]
        lista1[k + 1] = aux1
        k += 1

    if lista == lista1:
        return True

    if lista != lista1:
        return False
    return is_anagram(first_string, second_string)
