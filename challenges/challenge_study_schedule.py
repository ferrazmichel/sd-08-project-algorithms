import numbers


def study_schedule(permanence_period, target_time):
    if not isinstance(target_time, numbers.Number):
        return None
    result = 0
    try:
        for period in permanence_period:
            if period[1] >= target_time >= period[0]:
                result += 1
        return result
    except TypeError:
        return None
