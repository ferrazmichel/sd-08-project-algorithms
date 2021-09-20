# Solução parcial em:
# https://www.javatpoint.com/python-program-to-print-the-duplicate-elements-of-an-array
def find_duplicate(nums):
    """ Faça o código aqui. """
    result = None
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                result = nums[j]
    if not result or result < 0:
        return False
    return result
