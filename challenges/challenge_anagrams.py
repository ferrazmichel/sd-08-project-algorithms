# Algoritmo retirado do site ↓↓↓
# https://rosettacode.org/wiki/Sorting_algorithms/Quicksort#Python
def quick_sort(list):
    if not list:
        return []
    else:
        pivot = list[0]
        less = [x for x in list     if x <  pivot]
        more = [x for x in list[1:] if x >= pivot]
        return quick_sort(less) + [pivot] + quick_sort(more)

def is_anagram(first_string, second_string):
    first_string, second_string = quick_sort(list(first_string)), quick_sort(list=(second_string))
    if first_string == second_string:
        return True
    else:
        return False
