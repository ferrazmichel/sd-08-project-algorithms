def find_duplicate(nums):
    try:
        nums_sorted = sorted(nums)
        for i in range(len(nums_sorted) - 1):
            # if nums_sorted[i] < 0:
            #     return False
            if nums_sorted[i] == nums_sorted[i + 1]:
                return nums_sorted[i]
            else:
                i += 1
    except TypeError:
        return False
    return False
