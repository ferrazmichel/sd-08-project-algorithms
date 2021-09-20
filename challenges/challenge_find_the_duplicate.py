# https://docs.python.org/pt-br/3/tutorial/errors.html
# https://docs.python.org/pt-br/3/library/exceptions.html#AttributeError

def find_duplicate(nums):
    try:
        nums_sorted = sorted(nums)
        for i in range(0, len(nums_sorted) - 1):
            # if nums_sorted[i] < 0:
            #     return False
            if nums_sorted[i] < 0 or nums_sorted[i] != nums_sorted[i + 1]:
                i += 1
            else:
                return nums_sorted[i]
    except (TypeError, ValueError):
        return False
    return False
