# função auxiliar responsável pela partição do array
# escolhendo um pivô e fazendo movimentações dos sub arrays gerados
def partition(array, low, high):
    # índice do menor elemento
    i = low - 1
    # o pivô será escolhido
    # através do índice que divide o array
    pivot = array[high]  # pivot

    # itera sobre os elementos
    for j in range(low, high):

        # se o elemento corrente é menor ou igual ao pivô
        if array[j] <= pivot:

            # incrementa o índice do menor elemento
            i = i + 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]

    return i + 1


def quicksort(array, low, high):
    # caso base: se já atingiu a menor porção (1)
    if len(array) == 1:
        # retorne o array
        return array

    # os índices irão se cruzar quando o array estiver ordenado
    if low < high:
        # índice da partição é o índice onde o array foi divido
        # e é determinado a partir do pivô.
        # Este índice já está ordenado
        partition_index = partition(array, low, high)

        # Ordena os elementos presentes antes da partição (menores que o pivô)
        # e depois (maiores que o pivô)
        quicksort(array, low, partition_index - 1)
        quicksort(array, partition_index + 1, high)
    return array


def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    first_string_list = list(first_string)
    second_string_list = list(second_string)

    sort_first_string = quicksort(
        first_string_list, 0, len(first_string_list) - 1)
    sort_second_string = quicksort(
        second_string_list, 0, len(second_string_list) - 1)
    
    # print(sort_first_string)

    if sort_first_string == sort_second_string:
        # print('true')
        return True
    else:
        # print('false')
        return False


# first_string = 'pedra'
# second_string = 'perda'

# is_anagram(first_string, second_string)
