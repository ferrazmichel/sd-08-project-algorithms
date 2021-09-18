def is_anagram(first_string, second_string):
    """ Faça o código aqu. """
    if first_string == "" or second_string == "":
        return False
    if len(first_string) != len(second_string):
        return False

    lookup = {}

    for letter in first_string:
        if letter in lookup:
            lookup[letter] = lookup[letter]+1
        else:
            lookup[letter] = 1
    print(lookup)
    for item in second_string:
        print(item)
        if not lookup[item]:
            return False
        else:
            lookup[item] = lookup[item] - 1

    return True


is_anagram("pedra", "pedro")