def is_anagram(first_string, second_string):
    if first_string == '' or second_string == '':
        return False
    if first_string != second_string:
        return False
    if first_string == second_string:
        return True
