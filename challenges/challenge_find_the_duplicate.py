# def find_duplicate(nums):
#     """ Faça o código aqui. """
#     num_length = len(nums)
#     if nums is None or num_length == 1:
#         return False
#     for number_i in range(0, num_length):
#         if type(nums[number_i]) == str or nums[number_i] < 0:
#             return False
#         for number_j in range(number_i+1, num_length):
#             if(nums[number_i] == nums[number_j]):
#                 return nums[number_j]
#     return False


def find_duplicate(nums):
    """ Faça o código aqui. """
    num_length = len(nums)
    if nums is None or num_length == 1:
        return False
    sort_numbers = sorted(nums)
    for index in range(0, len(sort_numbers) - 1):
        if type(nums[index]) == str or nums[index] < 0:
            return False
        if(sort_numbers[index] == sort_numbers[index + 1]):
            return sort_numbers[index + 1]
    return False
