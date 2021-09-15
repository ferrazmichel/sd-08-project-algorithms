def find_duplicate(nums):
    counter = 0 
    if len(nums) <= 2:
        return False
    tested_number = nums[0]
    for number in nums[1:]:
        try:
            result = number > 0
        except TypeError:
            return False
        if result is True:
            return False
        if tested_number == number:
            counter += 1
    if counter == 1:
        return True
    else:
        return False
