def find_duplicate(nums):
    '''
    Returns the duplicate number if exists, False
    otherwise.
    '''
    if (
        not isinstance(nums, list)
        or len(nums) < 2
        or any((not isinstance(num, int) or num < 0) for num in nums)
    ):
        return False
    sorted_nums = sorted(nums)

    for index, num in enumerate(sorted_nums[:-1]):
        if num == sorted_nums[index + 1]:
            return num
    return False
