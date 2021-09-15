def check_duplicate(nums, num):
    if nums.count(num) > 1:
        return True
    return False


def find_duplicate(nums):
    num_duplicate = 0

    if len(nums) <= 1 or any(isinstance(num, str) or num < 0 for num in nums):
        return False

    for num in nums:
        if (check_duplicate(nums, num)):
            if (num_duplicate > 0 and num_duplicate != num):
                return False
            num_duplicate = num

    if (num_duplicate > 0):
        return num_duplicate
    return False
