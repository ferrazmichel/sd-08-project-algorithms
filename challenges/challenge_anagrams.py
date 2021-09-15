# https://wiki.python.org.br/QuickSort#CA-c1467e1644afb6fd403ca8e7e5bf18e1eb358ff5_6
def quicksort(arr):
    if len(arr) <= 1: return arr
    m = arr[0]
    return quicksort(filter(lambda i,j=m: i<j, arr)) + \
        filter(lambda i,j=m: i==j, arr) + \
        quicksort(filter(lambda i,j=m: i>j, arr))

def is_anagram(first_string, second_string):
    try:
        return (quicksort(list(first_string)) == quicksort(list(second_string)))
    except TypeError:
        return False