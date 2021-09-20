def quicksort(_l):
    if _l:
        left = [x for x in _l if x < _l[0]]
        right = [x for x in _l if x > _l[0]]
        if len(left) > 1:
            left = quicksort(left)
        if len(right) > 1:
            right = quicksort(right)
        return left + [_l[0]] * _l.count(_l[0]) + right
    return []

    """ Referência:
        https://wiki.python.org.br/QuickSort """


def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False
    if first_string == "" or second_string == "":
        return False
    first_list = quicksort(first_string)
    second_list = quicksort(second_string)

    return first_list == second_list
