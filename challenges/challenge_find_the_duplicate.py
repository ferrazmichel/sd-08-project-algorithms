def find_duplicate(nums):
    if not nums or type(nums) != list:
        return False

    # https://docs.python.org/pt-br/dev/howto/sorting.html
    nums_sorted = sorted(nums)

    found_number = None
    for num in nums_sorted:
        if type(num) != int or num <= 0:
            return False

        index = nums_sorted.index(num)

        new_array = nums_sorted.copy()
        new_array.pop(index)

        found_number = search_num(new_array, 0, len(new_array) - 1, num)

        if found_number:
            return found_number

    return found_number


def search_num(array, low_index, high_index, num):
    if high_index < low_index:
        return False

    middle_index = (low_index + high_index) // 2

    if array[middle_index] == num:
        return array[middle_index]
    elif array[middle_index] > num:
        return search_num(array, low_index, middle_index - 1, num)
    else:
        return search_num(array, middle_index + 1, high_index, num)
