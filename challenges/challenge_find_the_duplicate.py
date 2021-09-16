def find_duplicate(nums):
    size = len(nums)
    if size == 0:
        return False
    tested_number = size // 2
    try:
        result = nums[tested_number] < 1
    except TypeError:
        return False
    else:
        if result:
            return False
    bigger = [i for i in nums if i > tested_number]
    smaller = [i for i in nums if i <= tested_number]
    result_1 = recursive(bigger)
    result_2 = recursive(smaller)
    return result_1 or result_2


def recursive(nums):
    size = len(nums)
    bigger = []
    smaller = []
    if size >= 2:
        tested_number = nums[0]
        for number in nums[1:]:
            if number == tested_number:
                return number
            elif number < tested_number:
                smaller.append(number)
            else:
                bigger.append(number)
        result_1 = recursive(bigger)
        result_2 = recursive(smaller)
        return result_1 or result_2
    return False
