def find_duplicate(nums):
    for row in nums:
        if type(row) == str or row < 0:
            return False
        elif nums.count(row) > 1:
            return row
    return False
