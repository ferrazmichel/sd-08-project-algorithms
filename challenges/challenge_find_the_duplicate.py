def find_duplicate(nums):
    counter = 0
    size = len(nums)
    if size <= 2:
        return False
    tested_position = 0
    while tested_position < size:
        # tested_number = nums[tested_position]
        # for number in nums[tested_position + 1]:
        #     if number > 0 or counter == 2:
        #         return False
        #     if tested_number == number:
        #         counter += 1
        tested_position += 1
    if counter == 1:
        return True
