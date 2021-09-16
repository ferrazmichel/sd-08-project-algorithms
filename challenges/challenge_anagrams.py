def sort_string(string, criteria=None):
    """recebe uma string e ordena as letras
    em ordem alfabética"""
    string_list = list(string)
    for index in range(len(string_list) - 1):
        for index_2 in range(len(string_list) - 1):
            if string_list[index_2] > string_list[index_2 + 1]:
                string_list[index_2], string_list[index_2 + 1] = (
                    string_list[index_2 + 1],
                    string_list[index_2],
                )
    return "".join(string_list)


def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    return sort_string(first_string) == sort_string(second_string)


print(sort_string("caramelo"))
