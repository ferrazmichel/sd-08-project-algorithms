def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    if not isinstance(permanence_period, list) or not isinstance(
        target_time, int
    ):
        return None
    result = 0
    for number in permanence_period:
        if not isinstance(number[0], int) or not isinstance(number[1], int):
            return None
        if number[0] <= target_time <= number[1]:
            result += 1
    return result
