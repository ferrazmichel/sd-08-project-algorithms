def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    students_on_target_time = 0
    if target_time is None:
        return None
    for interval in permanence_period:
        if not isinstance(interval[0], int) or not isinstance(
            interval[1], int
        ):
            return None
        if interval[0] <= target_time <= interval[1]:
            students_on_target_time += 1
    return students_on_target_time
