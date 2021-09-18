def selection_sort(string):
    # como um algoritmo de força bruta
    # percorre a estrutura exaustivamente
    for i in range(len(string)):
        minimum = i

        # itera sobre os elementos não ordenados
        for j in range(i + 1, len(string)):
            # seleciona o menor valor
            if string[j] < string[minimum]:
                minimum = j
        # após encontrar o menor valor
        # ao invés de criar um novo array (aumenta complexidade de espaco)
        # realizamos a substituição entre o menor elemento
        # e a posição i que corresponde ao primeiro elemento não ordenado
        # que consequentemente passará a ser o último ordenado
        string[minimum], string[i] = string[i], string[minimum]

    return string


def is_anagram(first_string, second_string):
    first_sort = selection_sort(list(first_string))
    second_sort = selection_sort(list(second_string))

    return first_sort == second_sort
