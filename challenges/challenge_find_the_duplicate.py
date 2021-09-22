from challenges.challenge_anagrams import merge_sort


def find_duplicate(nums):
    if nums is None or len(nums) < 2:
        return False
    ordered_list = merge_sort(nums)
    if(type(ordered_list[0]) == str or ordered_list[0] < 0):
        return False
    for num in range(len(ordered_list) - 1):
        if(ordered_list[num] == ordered_list[num + 1]):
            return ordered_list[num]
    return False
