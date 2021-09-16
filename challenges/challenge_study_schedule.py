def study_schedule(permanence_period, target_time):
    if not isinstance(target_time, int):
        return None

    target_time_occurrence = 0

    for time_range in permanence_period:
        if not all(isinstance(n, int) for n in time_range):
            return None
        if time_range[0] <= target_time <= time_range[1]:
            target_time_occurrence += 1

    return target_time_occurrence
