def quantity_of_letters(word):
    letter_quantity = {}

    for letter in word:
        if letter in letter_quantity:
            letter_quantity[letter] = letter_quantity[letter]+1
        else:
            letter_quantity[letter] = 1
    return letter_quantity


def is_anagram(first_string, second_string):

    if first_string == "" or second_string == "":
        return False
    if len(first_string) != len(second_string):
        return False

    letter_quantity = quantity_of_letters(first_string)

    for item in second_string:
        if item not in letter_quantity or letter_quantity[item] == 0:
            return False
        else:
            letter_quantity[item] = letter_quantity[item] - 1
    return True
