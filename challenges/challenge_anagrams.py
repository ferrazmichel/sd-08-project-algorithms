from challenges.insertion_sort import insertion_sort


def is_anagram(first_string, second_string):
    sorted_first_string = insertion_sort(first_string)
    sorted_second_string = insertion_sort(second_string)

    if sorted_first_string == sorted_second_string:
        return True
    else:
        return False
