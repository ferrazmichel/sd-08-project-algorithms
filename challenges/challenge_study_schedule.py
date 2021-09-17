def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    try:
        occurrences = 0
        for schedule_range in permanence_period:
            if (
                schedule_range[0] <= target_time
                and schedule_range[1] >= target_time
            ):
                occurrences += 1
        return occurrences
    except TypeError:
        return None
