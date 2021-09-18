def find_duplicate(nums):
    """ Faça o código aqui. """
    if not isinstance(nums, list) or len(nums) <= 1:
        return False
    sorted_nums = sorted(nums)
    for index, number in enumerate(sorted_nums):
        if type(number) != int or number < 0 or index >= len(sorted_nums) - 1:
            return False
        if number == sorted_nums[index + 1]:
            return number
