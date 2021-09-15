def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """

    count = 0

    for student in permanence_period:
        if (
            student[0] is None
            or student[1] is None
            or target_time is None
        ):
            return None
        elif student[0] <= target_time <= student[1]:
            count += 1

    return count
