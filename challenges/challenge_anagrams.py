from merge_sort import merge_sort


def is_anagram(first_string, second_string):
    '''
    Returns True if the two strings are anagrams,
    False otherwise.
    '''
    return merge_sort(first_string) == merge_sort(second_string)
