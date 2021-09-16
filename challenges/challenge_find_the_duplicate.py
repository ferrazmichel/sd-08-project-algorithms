def find_duplicate(nums):
    """ Faça o código aqui. """
    if isinstance(nums, int) or isinstance(nums, str) or len(nums) > 2:
        return False
    for i in range(len(nums) - 2):
        if nums[i] in nums[i + 1:]:
            return nums[i]
    return False
