def count_letters(text):
    number_of_each_letter = {}
    for letter in text:
        if letter in number_of_each_letter:
            number_of_each_letter[letter] += 1
        else:
            number_of_each_letter[letter] = 1

    return number_of_each_letter


def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    return count_letters(first_string) == count_letters(second_string)
