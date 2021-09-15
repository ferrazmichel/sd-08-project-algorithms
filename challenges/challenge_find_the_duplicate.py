def find_duplicate(nums):
    if nums == [] or len(nums) == 1:
        return False
    freq_dict = {}
    for num in nums:
        if type(num) == str or num < 0:
            return False
        freq_dict[num] = freq_dict.get(num, 0) + 1
    max_value = max(freq_dict, key=freq_dict.get)
    min_value = min(freq_dict, key=freq_dict.get)
    if max_value == min_value and len(freq_dict) > 1:
        return False
    return max_value
