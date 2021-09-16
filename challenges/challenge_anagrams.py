# função construída conforme conteúdo do course
def bubble_sort(string):
    has_swapped = True
    num_of_iterations = 0

    while has_swapped:
        has_swapped = False

        for i in range(len(string) - num_of_iterations - 1):
            if string[i] > string[i + 1]:
                string[i], string[i + 1] = string[i + 1], string[i]
                has_swapped = True
        num_of_iterations += 1

    return string


def is_anagram(first_string, second_string):
    if not (first_string and second_string):
        return False

    if bubble_sort(list(first_string)) == bubble_sort(list(second_string)):
        return True

    return False
