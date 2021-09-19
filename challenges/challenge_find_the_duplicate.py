def find_duplicate(nums):
    sorted_nums = sorted(nums)
    for numA, numB in zip(sorted_nums, sorted_nums[1:]):
        if numA == numB and min(numA, numB) > 0:
            return numA
    return False
