def find_duplicate(nums):
    """ Faça o código aqui. """
    set_of_numbers = set({})
    for num in nums:
        if type(num) != int or num < 1:
            return False
        if num in set_of_numbers:
            return num
        else:
            set_of_numbers.add(num)

    return False
