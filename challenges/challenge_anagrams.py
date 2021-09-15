def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    if not first_string or not second_string:
        return False
    while len(first_string) != 0:
        char = first_string[0]
        first_string = first_string.replace(char, "")
        second_string = second_string.replace(char, "")

        if len(first_string) != len(second_string):
            return False
    return True
