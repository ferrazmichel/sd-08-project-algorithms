# UTILIZANDO BUBLE SORT NÃO PASSOU NO REQUISITO DO TEMPO
def sort_words(array):
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


# def is_anagram(first_string, second_string):
#     if len(first_string) == 0 or len(second_string) == 0:
#         return False

#     while len(first_string) > 0:
#         letter_to_take = first_string[0]
#         first_string = first_string.replace(letter_to_take, '')
#         second_string = second_string.replace(letter_to_take, '')

#         if(len(first_string) != len(second_string)):
#             return False

#     return True


def is_anagram(first_string, second_string):
    if len(first_string) == 0 or len(second_string) == 0:
        return False

    sorted_first_string = "".join(sort_words(list(first_string)))
    sorted_second_string = "".join(sort_words(list(second_string)))
    if sorted_first_string != sorted_second_string:
        return False
    return True
