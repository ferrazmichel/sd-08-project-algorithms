def find_duplicate(nums):
    """Faça o código aqui."""
    if not nums or len(nums) <= 1:
        return False
    frequency = {}
    for element in nums:
        if not isinstance(element, int) or element < 0:
            return False
        frequency[element] = frequency.get(element, 0) + 1

    list_values = list(frequency.values())
    list_keys = list(frequency.keys())
    if max(list_values) == 1:
        return False
    return list_keys[list_values.index(max(list_values))]
