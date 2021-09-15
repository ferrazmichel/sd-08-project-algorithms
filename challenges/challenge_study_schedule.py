def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    MAX_STUDENTS = 0
    try:
        for period in permanence_period:
            if period[0] <= target_time <= period[1]:
                MAX_STUDENTS += 1
    except TypeError:
        return None
    return MAX_STUDENTS
