def letters_number(word):
    letter_position = {}
    for letter in word:
        if letter in letter_position:
            letter_position[letter] += 1
        else:
            letter_position[letter] = 1

    return letter_position


def is_anagram(first_string, second_string):
    return letters_number(first_string) == letters_number(second_string)
