def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    if first_string == "" or second_string == "":
        return False
    lista = list(first_string)
    lista1 = list(second_string)
    if len(lista) != len(lista1):
        return False

    new_list = merge_sort(lista)
    new_list1 = merge_sort(lista1)

    if new_list == new_list1:
        return True
    else:
        return False
    # return is_anagram(first_string, second_string)


def merge_sort(array):
    # caso base: se já atingiu a menor porção (1)
    if len(array) <= 1:
        return array
    # calculo do pivot: índice que indica onde o array será particionado
    # no caso, metade
    mid = len(array) // 2
    # para cada metade do array
    # chama a função merge_sort de forma recursiva
    left, right = merge_sort(array[:mid]), merge_sort(array[mid:])
    # mistura as partes que foram divididas
    return merge(left, right, array.copy())
    # array = [1,4,5,62, 7,4,2]
    # left1 = [1,4,5] rigth1 = [62, 7, 4, 2]

    # array2 = [1,4,5]
    # left2 = [1] rigth2 = [4,5]

    # array3 = [62, 7, 4, 2]
    # left3 = [62, 7] --- rigth = [4,2]

    # ARRAY2.1 = [1]
    # array2.2 = [4,5]
    # left2.2 = [4]


# função auxiliar que realiza a mistura dos dois arrays
def merge(left, right, merged):

    left_cursor, right_cursor = 0, 0

    # enquanto nenhumas das partes é percorrida por completo
    while left_cursor < len(left) and right_cursor < len(right):

        # compare os dois itens das partes e insira no array de mistura o menor
        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor + right_cursor] = left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1
    # a iteração acima irá inserir os elementos de forma ordenada

    # quando uma das partes termina, devemos garantir
    # que a outra sera totalmente inserida no array de mistura

    # itera sobre os elementos restantes na partição "esquerda"
    # inserindo-os no array de mistura
    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]

    # itera sobre os elementos restantes na partição "direita"
    # inserindo-os no array de mistura
    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]

    return merged
