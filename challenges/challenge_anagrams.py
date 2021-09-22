def is_anagram(first_string, second_string):
    """ Compare two strings and return if its an anagram """
    if not first_string or not second_string:
        return False
    while len(first_string) != 0:
        character = first_string[0]
        first_string = first_string.replace(character, '')
        second_string = second_string.replace(character, '')
        if len(first_string) != len(second_string):
            return False
    return True
