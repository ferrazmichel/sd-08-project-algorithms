def find_duplicate(nums):
    if not nums:
        return False

    nums_copy = nums.copy()
    nums_copy.sort()

    for index in range(1, len(nums_copy)):
        if nums_copy[index] == nums_copy[index - 1]:
            return nums_copy[index]

    return False
