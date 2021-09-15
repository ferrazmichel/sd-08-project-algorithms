from challenges.smoothsort import smoothsort


def is_anagram(first_string, second_string):
    order_first = smoothsort(list(first_string))
    order_second = smoothsort(list(second_string))
    if order_first == order_second:
        return True
    return False
