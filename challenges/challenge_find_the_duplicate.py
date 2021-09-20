def find_duplicate(nums):
    if not nums:
        return False

    nums_copy = nums.copy()
    nums_copy.sort()

    for index in range(1, len(nums_copy)):
        num1 = nums_copy[index]
        num2 = nums_copy[index - 1]
        if num1 == num2 and min(num1, num2) > 0:
            return num1

    return False
