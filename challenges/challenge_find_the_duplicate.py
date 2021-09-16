def find_duplicate(nums):
    if not (
        all(isinstance(num, int) for num in nums) and
        all(num > 0 for num in nums)
    ):
        return False

    sorted_nums = sorted(nums)

    for index in range(len(sorted_nums) - 1):
        if sorted_nums[index] == sorted_nums[index + 1]:
            return sorted_nums[index]

    return False
