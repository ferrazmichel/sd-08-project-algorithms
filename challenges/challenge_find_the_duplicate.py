import collections


def find_duplicate(nums):
    if len(nums) == 0 or isinstance(nums[0], str) or nums[0] == -1:
        return False
    try:
        return ([item for item, count in
        collections.Counter(nums).items() if count > 1][0])
    except IndexError:
        return False
