def is_anagram(first_string, second_string):
    list_1 = [letter for letter in first_string]
    list_2 = [letter for letter in second_string]

    for index, letter in enumerate(list_1):
        letter_index = None

        for current_index in range(index, len(list_2)):
            if letter == list_2[current_index]:
                letter_index = list_2[current_index]
                break

        if not letter_index:
            break

        list_2[index], list_2[current_index] = (
            list_2[current_index],
            list_2[index],
        )

    return list_1 == list_2
