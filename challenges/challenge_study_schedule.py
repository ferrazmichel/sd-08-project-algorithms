def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    if type(target_time) != int:
        return None

    target_time_count = 0
    for period in permanence_period:
        if type(period[0]) != int or type(period[1]) != int:
            return None

        if period[0] <= target_time <= period[1]:
            target_time_count += 1

    return target_time_count
