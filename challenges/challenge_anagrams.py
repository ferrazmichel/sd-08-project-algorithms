from merge import merge_sort

def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False
    return merge_sort(first_string) == merge_sort(second_string)
