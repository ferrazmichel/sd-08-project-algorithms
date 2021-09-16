def find_duplicate(nums):
    size = len(nums)
    if size >= 2 and nums[0] > 0:
        recursive(nums)
    return False


def recursive(nums):
    size = len(nums)
    if size >= 2:
        bigger = []
        smaller = []
        tested_number = nums[0]
        for number in nums[1:]:
            if number > tested_number:
                bigger.append(number)
            elif number < tested_number:
                smaller.append(number)
            else:
                return tested_number
        recursive(smaller)
        recursive(bigger)
