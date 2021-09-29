def find_duplicate(nums):
    nums.sort()
    result = False
    for num, one_ahead in zip(nums, nums[1:]):
        if type(num) == int and num < 0:
            return False
        if num == one_ahead:
            return num
    return result
