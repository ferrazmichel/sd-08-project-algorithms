def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    students = 0
    if (target_time) is None:
        return None
    for start_time in permanence_period:
        if not isinstance(start_time[0], int) or not isinstance(
            start_time[1], int
        ):
            return None
        if start_time[0] <= target_time <= start_time[1]:
            students += 1
    return students
