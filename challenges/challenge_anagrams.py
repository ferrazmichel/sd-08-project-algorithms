# UTILIZANDO BUBLE SORT NÃO PASSOU NO REQUISITO DO TEMPO
# Source: Course Trybe
def sort_words_with_buble(array):
    has_swapped = True
    num_of_iterations = 0

    while has_swapped:
        has_swapped = False

        for i in range(len(array) - num_of_iterations - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                has_swapped = True
        num_of_iterations += 1

    return array


# UTILIZANDO O INSERTION SORT
# Source: Course Trybe
def sort_words_with_insertion_sort(array):
    for i in range(len(array)):
        current_value = array[i]
        current_position = i
        while (
            current_position > 0
            and array[current_position - 1] > current_value
        ):
            array[current_position] = array[current_position - 1]
            current_position = current_position - 1
        array[current_position] = current_value
    return array


# Dessa forma funciona e passa no requisito de tempo no entanto não utilizei
# algoritmo de ordenação

# def is_anagram(first_string, second_string):
#     # caso as strings estejam vazias retorna False
#     if len(first_string) == 0 or len(second_string) == 0:
#         return False

#     # Enquanto existam caracteres na first_string continua nesse bloco
#     while len(first_string) > 0:
#         # Inicia fazendo uma copia do primeiro caractere da first_string
#         letter_to_take = first_string[0]
#         # first_string vai receber ela mesmo sem os caracteres letter_to_take
#         first_string = first_string.replace(letter_to_take, '')
#         # second_string recebera ela mesmo sem os caracteres correspondentes
#         # ao primeiro caractere da first_string
#         second_string = second_string.replace(letter_to_take, '')
#         # Caso as strings tenham um tamanho diferente significa
#         # que tinham tamanhos diferentes
#         if(len(first_string) != len(second_string)):
#             return False

#     return True


def is_anagram(first_string, second_string):
    if len(first_string) == 0 or len(second_string) == 0:
        return False

    sorted_first_string = "".join(
        sort_words_with_insertion_sort(list(first_string))
    )
    sorted_second_string = "".join(
        sort_words_with_insertion_sort(list(second_string))
    )
    if sorted_first_string != sorted_second_string:
        return False
    return True
